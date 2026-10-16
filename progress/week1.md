# 진도 체크리스트: 1주차

직접 체크하는 진도 체크리스트입니다. 이 과정의 학습 경로이니 **위에서 아래로** 진행하세요.

> 📌 설치 및 준비를 마치기 전에는 이 체크리스트를 브라우저에서 **읽기만 하세요.** 설치 안내 마지막 단계에서 VS Code로 이 파일을 열고, 그때부터 체크합니다.

테스트 명령은 VS Code 터미널에 입력하세요. [어디에 입력합니까?](../docs/01-how-to-study.md#어디에-입력합니까)를 참고하세요.

**규칙:**

1. **순서대로** 진행하세요. **위의 모든 항목**을 체크한 뒤에만 다음 단계를 시작하세요.
   수업 파일은 위에서 아래로 읽으면서 중간의 "직접 해 보기"와 연습 문제를 **나오는 자리에서** 진행하세요. 체크리스트의 "수업 읽기"는 연습 문제 절 앞까지의 설명과 예제를 뜻합니다.
2. **정말 완료했을 때만** 체크하세요. 테스트 단계는 테스트가 통과해야 합니다.
3. VS Code 편집기에서 이 파일의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요. 단계를 마치면 바로 체크하세요.
4. 다른 작업 파일과 함께 이 파일을 커밋하고 푸시하세요. 멘토가 GitHub에서 진도를 확인합니다.

---

## 시작 준비

- [ ] 컴퓨터 설치 및 준비: [docs/00-setup.md](../docs/00-setup.md)
      ✔ `pytest exercises/week1/tests/test_w1d1.py`의 마지막 줄에 **2 failed**가 나오면 정상입니다. 아직 답을 작성하지 않아서 생기는 실패입니다.
      ✘ `command not found`, `ERROR`, `SyntaxError`처럼 테스트 실행 자체가 막히면 설치 안내 10단계를 다시 확인하세요.
- [ ] [이 과정의 공부 방법](../docs/01-how-to-study.md) 읽기
- [ ] [연습 문제 진행 방법](../docs/02-how-exercises-work.md) 1–3부 읽기

---

## 1일차: 터미널과 첫 프로그램

- [ ] [수업](../lessons/week1/day1-terminal-and-first-program.md)을 읽고 모든 예제를 직접 입력했습니다(연습 문제 절 앞까지)
- [ ] 수업의 "직접 해 보기"를 마쳤습니다
- [ ] 연습 문제 [`exercises/week1/w1d1_hello.py`](../exercises/week1/w1d1_hello.py)
- [ ] 연습 문제 [`exercises/week1/w1d1_robot_card.py`](../exercises/week1/w1d1_robot_card.py)
- [ ] 테스트 통과 ([`test_w1d1.py`](../exercises/week1/tests/test_w1d1.py)): `pytest exercises/week1/tests/test_w1d1.py` → **2 passed**
- [ ] `pwd`, `ls`, `cd`, `mkdir`을 찾아보지 않고 사용할 수 있습니다
- [ ] 실습 일지 작성: [`logs/`](../logs/)
- [ ] 커밋과 푸시 완료
- [ ] 멘토 점검

## 2일차: 변수, 숫자, 입력

- [ ] [수업](../lessons/week1/day2-variables-numbers-input.md)을 읽고 모든 예제를 직접 입력했습니다(연습 문제 절 앞까지)
- [ ] 수업의 "직접 해 보기"를 마쳤습니다
- [ ] 연습 문제 [`exercises/week1/w1d2_battery_runtime.py`](../exercises/week1/w1d2_battery_runtime.py)
- [ ] 연습 문제 [`exercises/week1/w1d2_time_format.py`](../exercises/week1/w1d2_time_format.py)
- [ ] 테스트 통과 ([`test_w1d2.py`](../exercises/week1/tests/test_w1d2.py)): `pytest exercises/week1/tests/test_w1d2.py` → **6 passed**
- [ ] `7`, `7.0`, `"7"`의 차이를 설명할 수 있습니다
- [ ] 실습 일지 작성
- [ ] 커밋과 푸시 완료
- [ ] 멘토 점검

## 3일차: 조건에 따라 판단하기, 함수와 `if` 문

- [ ] [수업](../lessons/week1/day3-functions-and-decisions.md)을 읽고 모든 예제를 직접 입력했습니다(연습 문제 절 앞까지)
- [ ] 수업의 "직접 해 보기"를 마쳤습니다
- [ ] [연습 문제 진행 방법](../docs/02-how-exercises-work.md) 4부 읽기(오늘부터 연습 문제는 함수입니다)
- [ ] 함수 `battery_status`: [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py)
- [ ] 함수 `can_launch`
- [ ] 함수 `classify_distance`
- [ ] 테스트 통과 ([`test_w1d3.py`](../exercises/week1/tests/test_w1d3.py)): `pytest exercises/week1/tests/test_w1d3.py` → **21 passed**
- [ ] `return`과 `print`의 차이, `=`와 `==`의 차이를 설명할 수 있습니다
- [ ] 실습 일지 작성
- [ ] 커밋과 푸시 완료
- [ ] 멘토 점검

## 4일차: 반복하기, `for` 문과 `while` 문

- [ ] [수업](../lessons/week1/day4-loops.md)을 읽고 모든 예제를 직접 입력했습니다(연습 문제 절 앞까지)
- [ ] 수업의 "직접 해 보기"를 마쳤습니다
- [ ] 함수 `countdown`: [`exercises/week1/w1d4_loops.py`](../exercises/week1/w1d4_loops.py)
- [ ] 함수 `sum_to`
- [ ] 함수 `steps_until_low` (먼저 종이에 표를 그리세요!)
- [ ] 테스트 통과 ([`test_w1d4.py`](../exercises/week1/tests/test_w1d4.py)): `pytest exercises/week1/tests/test_w1d4.py` → **12 passed**
- [ ] `range(2, 8, 2)`를 실행하지 않고 어떤 숫자가 나오는지 말할 수 있습니다
- [ ] 실습 일지 작성
- [ ] 커밋과 푸시 완료
- [ ] 멘토 점검

## 5일차: 문자열 다루기 + 주간 과제

오전:

- [ ] [수업](../lessons/week1/day5-strings-and-checkpoint.md)을 읽고 모든 예제를 직접 입력했습니다(연습 문제 절 앞까지)
- [ ] 수업의 "직접 해 보기"를 마쳤습니다
- [ ] 함수 `clean_command`: [`exercises/week1/w1d5_strings.py`](../exercises/week1/w1d5_strings.py)
- [ ] 함수 `make_topic_name`
- [ ] 함수 `is_valid_robot_id`
- [ ] 테스트 통과 ([`test_w1d5.py`](../exercises/week1/tests/test_w1d5.py)): `pytest exercises/week1/tests/test_w1d5.py` → **15 passed**
- [ ] 이번 주 전체 테스트 통과 ([`exercises/week1/`](../exercises/week1/)): `pytest exercises/week1` → **56 passed**

오후: 주간 과제([안내](../checkpoints/week1/README.md)). 금요일에 다 마치지 못하면 마친 부분까지 커밋하고 푸시한 뒤 멘토에게 알리세요. 다음 주 월요일 오전에 이어서 마칩니다.

- [ ] 주간 과제 안내 전체 읽기
- [ ] [`converter.py`](../checkpoints/week1/converter.py): 변환 함수 네 개 (`pytest checkpoints/week1 -k to_` → **4 passed**)
- [ ] `converter.py`: `main()`의 메뉴 작성, VS Code 터미널에서 직접 실행 완료 (`-k converter` → **2 passed**)
- [ ] [`guess.py`](../checkpoints/week1/guess.py): `check_guess` (`-k check_guess` → **3 passed**)
- [ ] `guess.py`: `main()`의 게임 작성, VS Code 터미널에서 직접 게임 실행 완료 (`-k guess_game` → **2 passed**)
- [ ] 테스트 통과 ([`checkpoints/week1/`](../checkpoints/week1/)): `pytest checkpoints/week1` → **11 passed**
- [ ] 실습 일지 작성
- [ ] 커밋하고 푸시했습니다. GitHub에서 최신 커밋에 ✅가 보입니다
- [ ] 멘토에게 두 프로그램을 보여 주고 코드를 설명했습니다

---

## 1주차 완료 🎉

- [ ] 위의 모든 항목을 체크했습니다

멘토가 2주차 자료를 올리면 다음 주 체크리스트(`progress/week2.md`)가 나타납니다. **Sync fork**로 받으세요([새 수업 받기](../docs/01-how-to-study.md#새-수업-받기) 참고).
