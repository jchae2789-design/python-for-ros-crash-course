# 이 과정의 공부 방법

## 어디에 입력합니까?

> 명령은 편집기 아래쪽 패널인 **VS Code 터미널**에 입력하세요. **Ctrl + `** 또는 **Terminal → New Terminal**로 엽니다.
> 터미널은 과정 폴더 `~/code/python-for-ros-crash-course`에서 시작하고 가상 환경이 활성화되어 있습니다. 프롬프트에 `(.venv)`가 보입니다.
> 다른 폴더에 있다면 VS Code 터미널에 `cd ~/code/python-for-ros-crash-course`를 입력하세요.
> `(.venv)`가 없으면 **휴지통 아이콘**으로 터미널을 닫고 새로 여세요. 그래도 없으면 VS Code 터미널에 `source .venv/bin/activate`를 입력하세요.
>
> `>>>` 뒤에 나오는 내용은 같은 VS Code 터미널 안의 **파이썬 `>>>` 프롬프트**에 입력하세요. `>>>`에서 입력한 내용은 파일에 저장되지 않습니다.
> 프롬프트 기호 `$`나 `>>>`는 입력하지 마세요.
> VS Code 터미널 명령으로 돌아가기 전에 파이썬 `>>>` 프롬프트에 `exit()`을 입력하세요.
>
> 파일은 터미널 위의 **VS Code 편집기**에서 수정하고 저장하세요.

## 매일 반복하는 공부 순서

[`progress/`](../progress/)의 체크리스트(예: [progress/week1.md](../progress/week1.md))에 모든 단계가 순서대로 나와 있습니다.
VS Code 편집기에서 체크리스트를 열고 위에서부터 차례로 진행하세요.
완료한 항목은 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

보통 하루는 다음과 같이 진행합니다.

1. **하루 시작하기:** VS Code를 여세요. 과정 폴더가 다시 열립니다. 그렇지 않으면 **File → Open Recent**에서 과정 폴더를 선택하세요. VS Code 편집기에서 [`progress/week1.md`](../progress/week1.md)를 여세요. **Ctrl + `**로 **VS Code 터미널**을 열고 프롬프트에 `(.venv)`가 있는지 확인하세요([어디에 입력합니까?](#어디에-입력합니까) 참고).
2. VS Code 편집기에서 [`lessons/week1/`](../lessons/week1/)의 **오늘 수업 파일을 읽으세요**.
   각 예제를 직접 입력하세요. 편집기나 파이썬 `>>>` 프롬프트를 사용하라는 수업 안내를 따르세요.

   파일에 작성하는 예제는 VS Code 터미널에 `code playground.py`를 입력해서 같은 창에 `playground.py`를 여세요.
   VS Code 편집기에서 `playground.py`에 예제를 입력하고 **Ctrl + S**로 `playground.py`를 저장하세요.

   VS Code 터미널에서 `python3 playground.py`를 실행하고 수업에 나온 결과와 비교하세요.

   VS Code 편집기에서 `playground.py`의 값을 하나 바꾸고 **Ctrl + S**로 `playground.py`를 저장하세요.
   VS Code 터미널에서 `python3 playground.py`를 다시 실행해서 차이를 확인하세요.
3. 오늘 수업 파일의 **"직접 해 보기"를 진행하세요**. 안내에 따라 VS Code 편집기에서 `playground.py`를 작성하고 VS Code 터미널에서 실행하거나, **파이썬 `>>>` 프롬프트**에서 대화형 실험을 해 보세요. 테스트는 없지만 연습 문제를 풀기 위한 준비입니다.
4. **연습 문제를 푸세요.** VS Code 편집기에서 오늘 수업에 나온 연습 문제 파일(예: [`w1d1_hello.py`](../exercises/week1/w1d1_hello.py))을 여세요.
   맨 위의 안내를 읽고 `TODO` 위치에 코드를 작성하세요. **Ctrl + S**로 저장하세요.
5. **테스트를 실행하세요.** VS Code 터미널에 방금 수정한 파일(예: `w1d1_hello.py`)의 연습 문제 진행 순서에 나온 `pytest` 명령을 입력하세요.
   결과를 수업에 나온 예상 테스트 개수와 비교하세요.
6. 멘토와 **점검**하세요. VS Code 편집기에서 연습 문제 파일(예: `w1d1_hello.py`)을 보여 주고 VS Code 터미널에서 결과를 보여 주세요.
7. VS Code 편집기에서 **날짜를 붙인 실습 일지**(`logs/YYYY-MM-DD.md`)를 쓰고 **[`progress/week1.md`](../progress/week1.md)를 체크하세요**. 두 파일을 **Ctrl + S**로 저장하세요. VS Code 터미널에서 [Git으로 작업 저장하기](#git으로-작업-저장하기)에 따라 이 파일들과 연습 문제 파일을 **커밋하고 푸시하세요**.

---

## 테스트 실행하기

테스트는 코드를 자동으로 확인해 줍니다. 예제를 포함한 전체 진행 순서는 VS Code 편집기에서 [연습 문제 진행 방법](02-how-exercises-work.md)을 열어 확인하세요. VS Code 터미널에 다음 명령을 입력하면 [`test_w1d3.py`](../exercises/week1/tests/test_w1d3.py)를 실행합니다.

```bash
pytest exercises/week1/tests/test_w1d3.py
```

결과는 다음과 같이 나올 수 있습니다.

- `5 passed`: 모두 통과했습니다. 🎉
- `2 failed, 3 passed`: 아직 틀린 부분이 있습니다.

### 실패한 테스트 읽는 방법

테스트가 실패하면 pytest가 다음과 비슷한 내용을 보여 줍니다.

```
FAILED exercises/week1/tests/test_w1d3.py::test_battery_status[89-OK]
    assert battery_status(percent) == expected
E   AssertionError: assert 'FULL' == 'OK'
```

다음처럼 읽으면 됩니다.

- `test_battery_status[89-OK]`: 테스트가 `battery_status(89)`를 호출했고 `"OK"`를 기대했습니다.
- `assert 'FULL' == 'OK'`: 함수는 `'FULL'`을 반환했지만, 기대한 값은 `'OK'`입니다.

VS Code 편집기에서 [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py)의 `battery_status`를 확인하세요. `percent`가 `89`일 때 조건을 차례대로 따라가 보세요. 함수가 `"OK"`를 반환해야 합니다.

### 유용한 pytest 옵션

VS Code 터미널에서 다음 명령으로 [3일차 테스트](../exercises/week1/tests/test_w1d3.py) 또는 [1주차 연습 문제 전체](../exercises/week1/)를 실행합니다.
각 명령이 어떤 결과를 보여 주는지는 주석에 나와 있습니다.

```bash
pytest exercises/week1/tests/test_w1d3.py -x          # 처음 실패하면 중단합니다
pytest exercises/week1/tests/test_w1d3.py -k status   # 이름에 "status"가 들어간 테스트만 실행합니다
pytest exercises/week1 --tb=line                      # 오류 메시지를 짧게 보여 줍니다
```

---

## 직접 코드 실행하기

테스트는 코드가 **올바른지** 알려 줍니다. 실패한 이유를 알아보려면 함수를 직접 호출해 보세요.

VS Code 터미널에서 아래 명령으로 [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py)를 불러오세요.
파이썬 `>>>` 프롬프트에 `battery_status(89)`를 입력하세요. 연습 문제를 풀었다면 `'OK'`가 나와야 합니다.
파이썬 `>>>` 프롬프트에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.

```bash
python3 -i exercises/week1/w1d3_conditions.py
```

```python
>>> battery_status(89)      # 어떤 값이 나옵니까?
```

VS Code 편집기에서 `w1d3_conditions.py`의 `battery_status` 안에 `print(...)`를 추가해서 변수 값을 표시하세요. **Ctrl + S**로 저장하세요.
파이썬이 아직 열려 있다면 `>>>`에 `exit()`을 입력하세요.
그런 다음 위의 불러오기 명령을 다시 실행하고 파이썬 `>>>` 프롬프트에서 `battery_status(89)`를 호출하세요.

오류를 찾고 고쳤으면 VS Code 편집기에서 `w1d3_conditions.py`에 추가한 `print(...)` 줄을 지우세요. **Ctrl + S**로 `w1d3_conditions.py`를 저장하세요.

---

## Git으로 작업 저장하기

매일 마칠 때(또는 그보다 자주) VS Code 편집기에서 연습 문제 파일, 날짜를 붙인 실습 일지, [`progress/week1.md`](../progress/week1.md)를 저장하세요. VS Code 터미널에 다음 명령을 순서대로 입력하세요.

```bash
git status                                  # 무엇을 바꿨는지 확인합니다
git add .                                   # 모든 변경 사항을 준비합니다
git commit -m "Week 1 Day 3: conditions"    # 메시지와 함께 저장합니다
git push                                    # GitHub로 보냅니다
```

커밋 메시지에는 **무엇을 했는지** 적으세요. `"update"`보다는 `"Week 1 Day 4: finish loops exercises"`처럼 쓰세요.

GitHub의 포크에서는 커밋 옆에 ✅ 또는 ❌가 보입니다. ❌는 아직 마치지 않은 연습 문제가 있다는 뜻일 뿐입니다. 주중에는 괜찮습니다. 금요일까지는 이번 주 테스트가 ✅가 되어야 합니다.

---

## 실습 일지

매일 아래 명령으로 [`logs/TEMPLATE.md`](../logs/TEMPLATE.md)를 복사하세요.
VS Code 터미널에 복사 명령을 입력하세요. 새 실습 일지에는 오늘 날짜를 사용합니다. 경로는 `logs/YYYY-MM-DD.md`입니다.

```bash
cp logs/TEMPLATE.md logs/$(date +%F).md
```

그런 다음 VS Code 편집기에서 해당 날짜의 파일을 여세요. 빈칸을 답으로 채우세요.
**Ctrl + S**로 저장하세요.

솔직하게 쓰세요. "`elif`를 이해하지 못했습니다"도 좋은 일지 내용입니다. 멘토가 어떤 도움을 줘야 할지 알 수 있기 때문입니다. 실습 일지는 공식 현장 실습 기록의 일부이기도 합니다.

---

## 막혔을 때

1. **VS Code 터미널에 나온 오류 메시지를 읽으세요.** 특히 **마지막 줄**을 보세요. 보통 무엇이 잘못됐는지 정확히 알려 줍니다.
2. 오류 메시지에 나온 연습 문제 파일을 VS Code 편집기에서 열고, 변수 값을 확인할 `print(...)`를 추가하세요. **Ctrl + S**로 파일을 저장하세요.
   수업의 진행 순서에 따라 연습 문제를 다시 실행하세요. 터미널에 변수 값이 보입니다.
3. VS Code 편집기에서 오늘 수업 파일 중 이 주제를 다룬 부분을 **다시 읽으세요**.
4. **20분**이 지나도 막혀 있습니까? VS Code 편집기에서 `logs/YYYY-MM-DD.md`에 질문을 적고 **Ctrl + S**로 저장한 뒤 멘토에게 물어보세요. 다음 내용을 보여 주세요.
   - 시도한 방법
   - 정확한 오류 메시지
   - 예상했던 결과

---

## 새 수업 받기

멘토가 원본 과정 저장소에 새 주차 자료를 추가합니다. 포크로 가져오려면 다음과 같이 하세요.

1. GitHub에서 포크를 열고 **Sync fork** → **Update branch**를 클릭하세요.
2. VS Code 터미널에 아래 명령을 순서대로 입력하세요. 새 수업을 내려받고 [`requirements.txt`](../requirements.txt)의 패키지를 설치합니다.
   VS Code에 새 주차 파일이 나타나야 합니다.
   ```bash
   git pull
   pip install -r requirements.txt
   ```
