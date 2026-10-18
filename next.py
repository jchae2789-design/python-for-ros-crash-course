"""진도 확인 도구입니다. 이 파일은 고치지 않아도 됩니다.

VS Code 터미널에서 `python3 next.py`를 실행하면 지금 할 일을 알려 줍니다.
- 연습 문제와 주간 과제는 테스트 결과로 자동으로 확인합니다.
- 실습 일지와 커밋/푸시도 자동으로 확인합니다.
- 테스트로 확인할 수 없는 단계(수업 읽기 등)는 질문으로 확인합니다.

결과는 progress/state.json과 PROGRESS.md에 저장됩니다.
`python3 next.py --report`는 질문 없이 진도표만 출력합니다(GitHub 자동 테스트에서 사용).
"""

import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROGRESS_DIR = ROOT / "progress"
STATE_FILE = PROGRESS_DIR / "state.json"
REPORT_FILE = ROOT / "PROGRESS.md"
TEST_TIMEOUT = 120  # 초


def load_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


MSG = load_json(PROGRESS_DIR / "messages.json", {})


def load_weeks():
    """progress/weekN_steps.json 파일을 주차 순서대로 읽습니다."""
    files = sorted(PROGRESS_DIR.glob("week*_steps.json"),
                   key=lambda p: int(p.stem[4:].split("_")[0]))
    return [load_json(p, None) for p in files]


def run_tests(paths):
    """pytest를 한 번 실행하고 {테스트 id: 통과 여부}를 돌려줍니다."""
    cmd = [sys.executable, "-m", "pytest", *paths, "-q", "-p", "no:cacheprovider",
           "--tb=no", "--color=no", "-rpfE",
           # 한 파일에 문법 오류가 있어도 나머지 테스트는 실행합니다.
           "--continue-on-collection-errors"]
    try:
        run = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                             encoding="utf-8", errors="replace", timeout=TEST_TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, "timeout"
    if "No module named pytest" in run.stderr:
        return None, "no_pytest"
    results = {}
    for line in run.stdout.splitlines():
        for word, ok in (("PASSED ", True), ("FAILED ", False), ("ERROR ", False)):
            if line.startswith(word):
                node = line[len(word):].split(" - ")[0].strip()
                results[node] = ok
    return results, None


def test_passed(step, results):
    """step의 테스트(경로와 -k 조건)에 해당하는 테스트가 모두 통과했는지 확인합니다."""
    matched = []
    k = step.get("k", "").lower()
    for node, ok in results.items():
        path, _, name = node.partition("::")
        in_path = any(path == p or path.startswith(p.rstrip("/") + "/") for p in step["paths"])
        if in_path and k in name.lower():
            matched.append(ok)
    return bool(matched) and all(matched)


def log_written():
    """오늘 날짜의 실습 일지가 있고, 빈칸(- 줄) 중 하나 이상에 내용을 적었으면 True입니다."""
    today = ROOT / "logs" / f"{datetime.date.today():%Y-%m-%d}.md"
    if not today.exists():
        return False
    filled = [line for line in today.read_text(encoding="utf-8").splitlines()
              if line.startswith("- ") and line[2:].strip()]
    return len(filled) > 0


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def pushed():
    """커밋하지 않은 변경이 없고, 푸시하지 않은 커밋도 없으면 True입니다."""
    status = git("status", "--porcelain")
    if status.returncode != 0 or status.stdout.strip():
        return False
    ahead = git("rev-list", "--count", "@{u}..HEAD")
    return ahead.returncode == 0 and ahead.stdout.strip() == "0"


def sync_progress():
    """진도 파일만 커밋하고 푸시합니다. 멘토 점검 답이 GitHub에도 바로 보이게 합니다."""
    files = ["progress/state.json", "PROGRESS.md"]
    git("add", *files)
    commit = git("commit", "-m", MSG["sync_commit"], "--", *files)
    if commit.returncode != 0:
        return
    push = git("push")
    print(MSG["synced"] if push.returncode == 0 else MSG["sync_failed"])


def is_done(step, state, results):
    kind = step["kind"]
    if kind == "test":
        return results is not None and test_passed(step, results)
    return step["id"] in state["done"]


def current_step(weeks, state, results):
    for week in weeks:
        for step in week["steps"]:
            if not is_done(step, state, results):
                return week, step
    return None, None


def ask(question):
    try:
        answer = input(f"{question} {MSG['yes_no']} ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    return answer in ("y", "yes", "ㅛ")


def section_title(week, key):
    return next(s["title"] for s in week["sections"] if s["key"] == key)


def print_overview(weeks, state, results, cur):
    for week in weeks:
        steps = week["steps"]
        done = sum(is_done(s, state, results) for s in steps)
        print(f"\n{week['title']}  {MSG['progress'].format(done=done, total=len(steps))}")
        for sec in week["sections"]:
            sec_steps = [s for s in steps if s["section"] == sec["key"]]
            if all(is_done(s, state, results) for s in sec_steps):
                mark = "✔"
            elif cur in sec_steps:
                mark = "▶"
            else:
                mark = " "
            print(f"  {mark} {sec['title']}")


def print_step(week, step):
    print(f"\n▶ {MSG['now']} ({section_title(week, step['section'])}): {step['label']}")
    for path in step.get("open", []):
        path = path.replace("{today}", f"{datetime.date.today():%Y-%m-%d}")
        print(f"   {MSG['open']}: {path}")
    if step.get("cmd"):
        print(f"   {MSG['test']}: {step['cmd']}")
    if step.get("note"):
        print(f"   {step['note']}")


def report(weeks, state, results):
    """PROGRESS.md와 GitHub 요약에 쓰는 진도표(Markdown)를 만듭니다."""
    _, cur = current_step(weeks, state, results)
    lines = [f"# {MSG['report_title']}", "", MSG["report_note"], ""]
    if cur:
        lines += [f"**{MSG['now']}:** {cur['label']}", ""]
    for week in weeks:
        steps = week["steps"]
        done = sum(is_done(s, state, results) for s in steps)
        lines += [f"## {week['title']} ({done} / {len(steps)})", ""]
        for sec in week["sections"]:
            lines += [f"### {sec['title']}", ""]
            for s in steps:
                if s["section"] != sec["key"]:
                    continue
                mark = "✅" if is_done(s, state, results) else ("▶️" if s is cur else "⬜")
                lines.append(f"- {mark} {s['label']}")
            lines.append("")
    return "\n".join(lines)


def save(state, weeks, results):
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8", newline="\n")
    REPORT_FILE.write_text(report(weeks, state, results), encoding="utf-8", newline="\n")


def main():
    weeks = [w for w in load_weeks() if w]
    state = load_json(STATE_FILE, {"done": []})
    paths = sorted({p for w in weeks for s in w["steps"] if s["kind"] == "test" for p in s["paths"]})
    results, error = run_tests(paths)
    # pytest가 실행되면 설치 및 준비가 끝난 것입니다.
    for week in weeks:
        for step in week["steps"]:
            if step["kind"] == "setup" and results is not None and step["id"] not in state["done"]:
                state["done"].append(step["id"])

    if "--report" in sys.argv:
        print(report(weeks, state, results))
        return

    if error:
        # 테스트 결과를 모르면 진도를 저장하지 않습니다(이미 저장된 진도가 지워지지 않도록).
        print(MSG[error])
        return

    shown = False
    while True:
        week, step = current_step(weeks, state, results)
        # 실습 일지와 커밋/푸시는 지금 할 단계일 때만 자동으로 확인합니다.
        if step and step["kind"] == "log" and log_written():
            state["done"].append(step["id"])
            continue
        if step and step["kind"] == "git" and pushed():
            state["done"].append(step["id"])
            continue

        if not shown:
            print_overview(weeks, state, results, step)
            shown = True
        if step is None:
            print(f"\n{MSG['all_done']}")
            break
        print_step(week, step)
        if step["kind"] == "manual":
            if ask(step["ask"]):
                state["done"].append(step["id"])
                save(state, weeks, results)
                print(MSG["saved"])
                if step.get("sync"):
                    sync_progress()
                continue
            print(f"\n{MSG['come_back']}")
            break
        print(f"\n{MSG['after_' + step['kind']]}")
        break

    save(state, weeks, results)


if __name__ == "__main__":
    main()
