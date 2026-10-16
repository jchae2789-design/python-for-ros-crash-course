# ROS를 위한 파이썬: 4주 집중 과정

반갑습니다! 이 과정에서는 프로그래밍을 처음 배우는 사람도 4주 동안 파이썬을 단계별로 익힐 수 있습니다. 과정을 마치면 **ROS 2**(로봇 운영 체제)로 실제 로봇을 프로그래밍할 준비가 됩니다.

**혼자서** 자기 속도에 맞춰 공부합니다. 멘토가 매일 진행 상황을 점검합니다. 모든 연습 문제에는 코드가 올바른지 알려 주는 **자동 테스트**가 있습니다.

---

## 여기서 시작하세요

👉 **[progress/week1.md](progress/week1.md)를 열고 위에서부터 순서대로 진행하세요.**

설치 및 준비를 마친 뒤에는 VS Code 편집기에서 완료한 항목을 체크합니다.
[어디에 입력합니까?](docs/01-how-to-study.md#어디에-입력합니까)를 참고하세요.

이 체크리스트에는 설치 및 준비, 읽을 자료, 모든 수업과 연습 문제가 일주일 동안 진행할 순서대로 나와 있습니다. 각 단계를 마치면 직접 체크하고, 위의 항목을 모두 체크한 뒤에만 다음으로 넘어가세요.

체크리스트의 첫 단계는 다음과 같습니다.

1. **컴퓨터 설치 및 준비:** 브라우저에서 [docs/00-setup.md](docs/00-setup.md)를 여세요(약 1–2시간).
2. **이 과정의 공부 방법:** 브라우저나 VS Code 편집기에서 [docs/01-how-to-study.md](docs/01-how-to-study.md)를 여세요(10분).
3. **연습 문제와 테스트 진행 방법:** 브라우저나 VS Code 편집기에서 [docs/02-how-exercises-work.md](docs/02-how-exercises-work.md)를 여세요(20분).
4. **1주차 1일차:** 브라우저나 VS Code 편집기에서 [lessons/week1/day1-terminal-and-first-program.md](lessons/week1/day1-terminal-and-first-program.md)를 여세요.

---

## 일정

| 주차 | 날짜(2026년) | 주제 | ROS에서 필요한 이유 | 주간 과제(체크포인트) |
|---|---|---|---|---|
| **1** | 10월 19일 – 10월 23일 | 터미널과 파이썬 기초 | 터미널에서 ROS를 제어합니다 | 로봇 콘솔 도구(단위 변환기 + 숫자 맞히기 게임) |
| **2** | 10월 26일 – 10월 30일 | 데이터와 함수 | ROS 메시지는 구조가 있는 데이터입니다 | 센서 데이터 분석기 |
| **3** | 11월 2일 – 11월 6일 | 코드 정리: 클래스, 모듈, 오류 | 모든 ROS 노드는 클래스입니다 | 로봇 클래스 계층 |
| **4** | 11월 9일 – 11월 13일 | ROS 방식의 코드: 콜백, 타이머, 발행/구독 | 실제 ROS 2에서도 같은 개념을 사용합니다 | **mini-ROS**: 작은 ROS 직접 만들기 |

2–4주차 자료는 학습할 때가 되면 이 저장소에 올라옵니다. [새 수업 받기](docs/01-how-to-study.md#새-수업-받기)를 참고하세요.

### 1주차

| 일차 | 수업 | 연습 문제 |
|---|---|---|
| 1 | [터미널과 첫 프로그램](lessons/week1/day1-terminal-and-first-program.md) | [`exercises/week1/w1d1_*.py`](exercises/week1/) |
| 2 | [변수, 숫자, 입력](lessons/week1/day2-variables-numbers-input.md) | `exercises/week1/w1d2_*.py` |
| 3 | [조건에 따라 판단하기: 함수와 if 문](lessons/week1/day3-functions-and-decisions.md) | [`exercises/week1/w1d3_conditions.py`](exercises/week1/w1d3_conditions.py) |
| 4 | [반복하기: for 문과 while 문](lessons/week1/day4-loops.md) | [`exercises/week1/w1d4_loops.py`](exercises/week1/w1d4_loops.py) |
| 5 | [문자열 다루기 + 주간 과제](lessons/week1/day5-strings-and-checkpoint.md) | [`exercises/week1/w1d5_strings.py`](exercises/week1/w1d5_strings.py), [주간 과제](checkpoints/week1/README.md) |

---

## 수업을 진행하는 방법

수업은 **하나의 경로**를 따라 진행합니다. 단계를 건너뛰지 말고 항상 바로 다음 단계를 진행하세요.

```
설치 및 준비 → 1일차 → 2일차 → 3일차 → 4일차 → 5일차 + 주간 과제 → 2주차 → ... → 4주차 → ROS 2
```

[`progress/`](progress/)의 체크리스트를 보면 지금 어느 단계인지 정확히 알 수 있습니다.

### 1단계: 지금 할 일 찾기

VS Code 편집기에서 이번 주 체크리스트를 여세요. 예를 들어 [progress/week1.md](progress/week1.md)를 열면 됩니다. **아직 체크하지 않은 첫 번째 항목이 다음에 할 일입니다.**

```markdown
- [x] 수업을 읽고 모든 예제를 직접 입력했습니다
- [x] 수업의 "직접 해 보기"를 마쳤습니다
- [ ] 연습 문제 `exercises/week1/w1d1_hello.py`      ← 지금 할 일입니다
- [ ] 연습 문제 `exercises/week1/w1d1_robot_card.py`
```

### 2단계: 해당 단계 진행하기

[`progress/week1.md`](progress/week1.md)에서 체크하지 않은 첫 번째 항목 옆의 안내를 읽으세요. 링크된 안내 문서나 수업을 브라우저 또는 VS Code에서 여세요. 연습 문제는 [연습 문제 진행 방법](docs/02-how-exercises-work.md)을 참고하세요.

### 3단계: 정말 마쳤는지 확인하기

- **수업 읽기:** 모든 예제를 직접 입력하고 실행했습니다.
- **연습 문제:** 직접 풀었고, 안내한 대로 동작합니다.
- **"테스트 통과" 항목:** VS Code 터미널에 해당 항목 옆의 `pytest` 명령을 입력하세요. 결과가 예를 들어 `21 passed`처럼 **정확히** 일치해야 합니다.
- **"…을(를) 설명할 수 있습니다" 항목:** 수업을 보지 않고 해당 개념을 혼자 소리 내어 설명해 보세요. 설명하기 어렵다면 수업의 해당 부분을 다시 읽으세요.

### 4단계: 체크하기

VS Code 편집기에서 [`progress/week1.md`](progress/week1.md)를 여세요. 완료한 항목 옆의 `[ ]`를 `[x]`로 바꾸세요(x는 소문자이고 공백은 없습니다).
**Ctrl + S**로 저장하세요.

```markdown
- [ ] 연습 문제 `exercises/week1/w1d1_hello.py`      ← 체크 전
- [x] 연습 문제 `exercises/week1/w1d1_hello.py`      ← 체크 후
```

푸시하면 GitHub에서 체크리스트가 실제 체크박스로 보입니다.

그런 다음 **1단계**로 돌아가세요.

### 매일 마칠 때

하루의 마지막 항목은 실습 일지 작성, 커밋과 푸시, 멘토 점검입니다. 코드, 실습 일지, [`progress/week1.md`](progress/week1.md)를 저장하세요. 그런 다음 VS Code 터미널에 다음 명령을 순서대로 입력하세요.

```bash
git add .
git commit -m "Week 1 Day 1: finished exercises"
git push
```

멘토는 GitHub에서 포크를 열어 체크리스트, 코드, 실습 일지, 테스트 통과 여부(✅ 또는 ❌)를 확인합니다.

### 다음 날로 넘어가기

**N일차의 모든 항목**을 체크한 뒤에만 **N + 1일차**를 시작하세요. 일찍 끝나면 "추가 도전"을 해 보거나 어려웠던 부분을 다시 읽으세요. 다음 날 수업을 미리 시작하지 마세요.

### 다음 주로 넘어가기

다음 조건을 모두 만족하면 한 주를 마친 것입니다.

1. **"N주차 완료"**를 포함해 이번 주 체크리스트의 모든 항목을 체크했습니다.
2. 이번 주 주간 과제가 테스트를 통과했습니다.
3. 멘토에게 주간 과제를 보여 주었습니다.

그런 다음 다음 주 자료를 받으세요.

1. 브라우저에서 GitHub의 포크를 열고 **Sync fork** → **Update branch**를 클릭하세요.
2. VS Code 터미널에 `git pull`을 입력하세요. VS Code 편집기에 새 주차 파일이 나타나야 합니다.
3. VS Code 편집기에서 새 체크리스트(예: `progress/week2.md`)를 열고, 아직 체크하지 않은 첫 단계부터 진행하세요.

### 하루 일과 예시

```
오전        오늘 수업을 읽습니다. 모든 예제를 직접 입력합니다(복사해서 붙여 넣지 마세요).
오후        연습 문제를 풉니다. 통과할 때까지 테스트를 실행합니다.
멘토 점검   멘토와 15분 동안 확인합니다. 결과물을 보여 주고 궁금한 점을 질문합니다.
마칠 때     실습 일지를 쓰고, 체크리스트를 체크한 뒤 커밋하고 푸시합니다.
```

---

## 규칙

- **붙여 넣지 말고 직접 입력하세요.** 손으로 입력하는 것도 연습입니다.
- **20분 동안 시도한 뒤 질문하세요.** 20분 동안 막히는 건 자연스럽습니다. 하지만 2시간을 계속 쓰는 건 아깝습니다. 실습 일지에 질문을 적고 멘토에게 물어보세요.
- **AI 도구**(ChatGPT, Claude, Copilot 등)에는 **오류 메시지나 개념을 설명해 달라**고 물어봐도 됩니다. 연습 문제나 주간 과제 코드를 대신 작성해 달라고 하면 **안 됩니다**. 멘토가 코드를 한 줄씩 설명해 보라고 할 것입니다.
- **매일 푸시하세요.** 멘토가 GitHub에서 진도를 확인합니다.
- **[`tests/`](exercises/week1/tests/) 폴더는 절대 수정하지 마세요.** 테스트가 통과하도록 코드를 고치세요. 코드에 맞춰 테스트를 고치면 안 됩니다.

---

## 저장소 구성

```
README.md           ← 지금 읽고 있는 파일입니다
docs/               설치 및 준비, 공부 방법 안내
lessons/weekN/      수업 자료: 읽을 파일입니다
exercises/weekN/    연습 문제 파일: 여기에 코드를 작성합니다
exercises/weekN/tests/   자동 테스트(수정하지 마세요)
checkpoints/weekN/  주간 과제
logs/               실습 일지(TEMPLATE.md를 복사하세요)
progress/           주차별 체크리스트: 순서대로 진행하세요
```

## 유용한 명령

VS Code 터미널에서 다음 명령으로 [3일차 테스트](exercises/week1/tests/test_w1d3.py), [1주차 연습 문제](exercises/week1/), [주간 과제 테스트](checkpoints/week1/)를 실행합니다.
주석에는 각 명령이 실행하는 테스트가 나와 있습니다. 1주차를 마친 뒤에는 순서대로 `21 passed`, `64 passed`, `11 passed`, `75 passed`가 나와야 합니다.

```bash
pytest exercises/week1/tests/test_w1d3.py   # 하루치 테스트
pytest exercises/week1                      # 한 주 전체 테스트
pytest checkpoints/week1                    # 주간 과제 테스트
pytest                                      # 모든 테스트
```
