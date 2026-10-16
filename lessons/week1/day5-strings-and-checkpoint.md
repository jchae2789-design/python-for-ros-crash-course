# 1주차 · 5일차: 문자열 다루기 + 주간 과제

**배울 내용:** 문자열에서 글자 하나나 일부를 꺼내는 방법, 자주 쓰는 문자열 메서드, 문자열을 반복문으로 살펴보는 방법을 배워요. 오후에는 1주차 주간 과제를 만들어요.

**로봇을 다룰 때 필요한 이유:** ROS에서는 `/rail_robot/lidar` 같은 토픽, 로봇 식별 번호, 명령, 로그 메시지를 모두 문자열로 나타내요. 이런 이름을 확인하고, 정리하고, 만드는 일을 자주 하게 돼요.

---

## 1. 인덱싱: 글자 하나 꺼내기

문자열의 각 글자에는 **0**부터 시작하는 위치 번호(**인덱스**)가 있어요.

```
 text:   R   R   -   0   0   4   2
 index:  0   1   2   3   4   5   6
 from end: -7  -6  -5  -4  -3  -2  -1
```

```python
robot_id = "RR-0042"
print(robot_id[0])     # R
print(robot_id[2])     # -
print(robot_id[-1])    # 2   (음수는 끝에서부터 세요)
print(len(robot_id))   # 7   (글자 수)
```

`robot_id[7]`은 `IndexError: string index out of range`를 일으켜요. 마지막 인덱스는 길이에서 1을 뺀 `len - 1`이에요.

---

## 2. 슬라이싱: 문자열 일부 꺼내기

`text[start:stop]`은 `start`부터 `stop` 직전까지의 글자를 꺼내요. `stop`은 **포함하지 않아요**(`range`와 같아요).

```python
robot_id = "RR-0042"
print(robot_id[0:2])   # RR
print(robot_id[3:7])   # 0042
print(robot_id[3:])    # 0042   (끝을 생략하면 마지막까지 꺼내요)
print(robot_id[:2])    # RR     (시작을 생략하면 처음부터 꺼내요)
```

### 직접 해 보기

VS Code 터미널에 `python3`를 입력하세요. 파이썬 `>>>` 프롬프트에 `topic = "/drone/camera"`를 입력하고, `topic`을 슬라이싱해서 `drone`과 `camera`를 꺼내세요. 파이썬에 `'drone'`과 `'camera'`가 나와야 해요. 마지막으로 `>>>`에 `exit()`을 입력하세요.

---

## 3. 문자열 메서드

**메서드**는 값에 속한 함수예요. `text.method()`처럼 점을 붙여서 호출해요.

| 메서드 | 하는 일 | 예 | 결과 |
|---|---|---|---|
| `.lower()` | 모두 소문자로 바꿔요 | `"LiDAR".lower()` | `"lidar"` |
| `.upper()` | 모두 대문자로 바꿔요 | `"stop".upper()` | `"STOP"` |
| `.strip()` | 양 끝의 공백과 줄바꿈을 없애요 | `"  go \n".strip()` | `"go"` |
| `.replace(a, b)` | 모든 `a`를 `b`로 바꿔요 | `"rail robot".replace(" ", "_")` | `"rail_robot"` |
| `.startswith(x)` | x로 시작하나요? | `"/drone".startswith("/")` | `True` |
| `.endswith(x)` | x로 끝나나요? | `"scan.csv".endswith(".csv")` | `True` |
| `.isdigit()` | 0–9의 숫자로만 되어 있나요? | `"0042".isdigit()` | `True` |
| `.isalpha()` | 문자로만 되어 있나요? | `"RR".isalpha()` | `True` |
| `.isupper()` | 모든 문자가 대문자인가요? | `"RR".isupper()` | `True` |

문자열 자체는 **바꿀 수 없어요**. 중요한 점이에요. 메서드는 **새** 문자열을 돌려줘요. VS Code에서 `playground.py`에 아래처럼 새 문자열을 `command`에 다시 저장하세요.

```python
command = "  FORWARD  "
command.strip()             # command 자체는 바뀌지 않아요!
command = command.strip()   # ✅ 새 문자열을 저장해요
```

메서드를 **이어 붙일 수 있어요**. 왼쪽부터 오른쪽 순서로 실행돼요. VS Code 터미널에 `python3`를 입력한 뒤 `>>>`에 아래 식을 입력하면 `'turn left'`가 나와요. 마지막으로 `>>>`에 `exit()`을 입력하세요.

```python
"  Turn LEFT  ".strip().lower()     # "turn left"
```

### 문자열 이어 붙이기

`+`는 문자열을 이어 붙여요.

```python
robot = "drone"
topic = "/" + robot + "/camera"     # "/drone/camera"
```

f-문자열을 쓰면 더 읽기 쉬울 때가 많아요: `f"/{robot}/camera"`.

---

## 4. `in`: 안에 들어 있나요?

```python
print("lidar" in "/rail_robot/lidar")    # True
print("x" in "robot")                    # False
```

---

## 5. 문자열을 반복문으로 살펴보기

`for` 문은 문자열을 한 글자씩 살펴볼 수 있어요.

```python
for ch in "ROS":
    print(ch)
```

```
R
O
S
```

4일차에 배운 누적 방법과 함께 사용할 수 있어요.

```python
digits = 0
for ch in "RR-0042":
    if ch.isdigit():
        digits = digits + 1
print(digits)       # 4
```

---

## 6. 자주 하는 실수

| 실수 | 해결 방법 |
|---|---|
| `text.lower()`가 "동작하지 않아요" | 결과를 저장하세요: `text = text.lower()` |
| `IndexError: string index out of range`가 나와요 | 마지막 인덱스는 `len(text) - 1`이에요 |
| `text[0:2]`에서 글자가 3개가 아니라 2개 나와요 | 끝 인덱스는 포함하지 않아요 |
| `"robot".upper`를 출력하면 `<built-in method ...>`가 나와요 | 메서드에는 괄호가 필요해요: `.upper()` |

---

## 7. 연습 문제(오전)

**연습 문제 진행 방법:** 한 번에 하나씩 **순서대로** 푸세요. 아래의 각 연습 문제에는 번호가 붙은 진행 순서가 있어요. 1번부터 끝까지 따라 한 뒤 다음 연습 문제로 넘어가세요. 잘되지 않는 단계가 있으면 [연습 문제 진행 방법 5부](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 참고하세요.

네 함수는 모두 [`exercises/week1/w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)에 있어요. 아래에서 각 함수의 번호가 붙은 진행 순서를 따르세요.

### 연습 문제 1/4: `clean_command(text)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 양 끝의 공백과 줄바꿈을 없애고 문자열을 소문자로 바꾸세요.

```python
>>> clean_command("  FORWARD \n")
'forward'
```

**따라 해 볼 예제:** 비슷한 문제예요(이 연습 문제의 정답은 아니에요).

이 함수는 이름표의 문자열을 정리하고 **대문자**로 바꿔요. 두 메서드를 왼쪽에서 오른쪽으로 이어 붙여요.

```python
def make_label(text):
    return text.strip().upper()
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과예요.

```python
$ python3 -i playground.py
>>> make_label('  rail robot \n')
'RAIL ROBOT'
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 편집기에서 [`exercises/week1/w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열려요. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d5_strings.py`의 `clean_command` 안에 있는 `pass`를 코드로 바꾸세요. 3절의 메서드 두 개를 이어 붙이면 돼요.
3. VS Code 편집기에서 **Ctrl + S**로 `w1d5_strings.py`를 저장하세요. 파일 탭의 **●**가 사라져요.

   VS Code 터미널에서 `python3 -i exercises/week1/w1d5_strings.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `clean_command(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w1d5.py`](../../exercises/week1/tests/test_w1d5.py)로 `clean_command`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k clean_command
   ```
   ✔ `3 passed, 16 deselected`가 나와야 해요.
5. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)를 여세요.
   `clean_command` 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

> `deselected`는 이 파일에 있는 **다른** 연습 문제의 테스트는 실행하지 않았다는 뜻이에요. `-k`를 사용하면 이렇게 되니 괜찮아요.

### 연습 문제 2/4: `make_topic_name(robot_name, sensor)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** ROS 토픽 이름을 만드세요. 모두 소문자로 바꾸고, 공백을 `_`로 바꾸고, `/<robot>/<sensor>` 형태로 이어 붙이세요.

```python
>>> make_topic_name("Rail Robot 1", "LiDAR")
'/rail_robot_1/lidar'
```

**따라 해 볼 예제:** 비슷한 문제예요(이 연습 문제의 정답은 아니에요).

이 함수는 로그 파일 이름을 만들어요. 소문자로 바꾸고, 공백을 `-`로 바꾸고, 각 부분을 `_`로 이어 붙인 뒤 끝에 `.csv`를 붙여요.

```python
def make_file_name(robot_name, date):
    robot = robot_name.lower().replace(" ", "-")
    return robot + "_" + date + ".csv"
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과예요.

```python
$ python3 -i playground.py
>>> make_file_name('Rail Robot 1', '2026-10-19')
'rail-robot-1_2026-10-19.csv'
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 편집기에서 [`exercises/week1/w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열려요. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d5_strings.py`의 `make_topic_name` 안에 있는 `pass`를 코드로 바꾸세요. 각 부분을 `.lower()`와 `.replace(" ", "_")`로 정리한 뒤 `"/"`로 이어 붙이세요(3절의 "문자열 이어 붙이기").
3. VS Code 편집기에서 **Ctrl + S**로 `w1d5_strings.py`를 저장하세요. 파일 탭의 **●**가 사라져요.

   VS Code 터미널에서 `python3 -i exercises/week1/w1d5_strings.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `make_topic_name(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w1d5.py`](../../exercises/week1/tests/test_w1d5.py)로 `make_topic_name`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k make_topic_name
   ```
   ✔ `3 passed, 16 deselected`가 나와야 해요.
5. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)를 여세요.
   `make_topic_name` 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

### 연습 문제 3/4: `is_valid_robot_id(robot_id)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 문자열이 `RR-0042` 형태이면 `True`를 반환하세요. 정확히 7글자이고 대문자 두 개, `-`, 숫자 네 개 순서여야 해요. 그 밖의 경우에는 `False`를 반환하세요.

```python
>>> is_valid_robot_id("RR-0042")
True
>>> is_valid_robot_id("rr-0042")
False
>>> is_valid_robot_id("RR0042")
False
```

**따라 해 볼 예제:** 비슷한 문제예요(이 연습 문제의 정답은 아니에요).

이 함수는 문자열이 `09:30`처럼 `HH:MM` 형태의 시간인지 확인해요. 먼저 길이를 확인하고, 슬라이싱으로 각 부분을 확인해요.

```python
def is_valid_time(text):
    if len(text) != 5:
        return False
    if not text[0:2].isdigit():
        return False
    if text[2] != ":":
        return False
    return text[3:].isdigit()
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과예요.

```python
$ python3 -i playground.py
>>> is_valid_time('09:30')
True
>>> is_valid_time('9:30')
False
>>> is_valid_time('09-30')
False
>>> is_valid_time('')
False
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 편집기에서 [`exercises/week1/w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열려요. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d5_strings.py`의 `is_valid_robot_id` 안에 있는 `pass`를 코드로 바꾸세요. **다음 순서대로** 확인하세요.
   1. VS Code 편집기에서 `w1d5_strings.py`에 `len(robot_id)`가 정확히 7인지 확인하는 코드를 작성하세요. 7이 아니면 바로 `return False`로 반환하세요. 길이를 먼저 확인하지 않으면 짧은 문자열에서 `robot_id[2]` 때문에 오류가 날 수 있어요.
   2. VS Code 편집기에서 `w1d5_strings.py`에 앞의 두 글자(`robot_id[0:2]`)가 문자**이면서** 대문자인지 확인하는 코드를 작성하세요.
   3. VS Code 편집기에서 `w1d5_strings.py`에 인덱스 2의 글자(`robot_id[2]`)가 `"-"`인지 확인하는 코드를 작성하세요.
   4. VS Code 편집기에서 `w1d5_strings.py`에 마지막 네 글자(`robot_id[3:]`)가 숫자인지 확인하는 코드를 작성하세요.
3. VS Code 편집기에서 **Ctrl + S**로 `w1d5_strings.py`를 저장하세요. 파일 탭의 **●**가 사라져요.

   VS Code 터미널에서 `python3 -i exercises/week1/w1d5_strings.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `is_valid_robot_id(...)` 호출을 입력하고 결과를 비교하세요. `>>>`에 `is_valid_robot_id("")`도 입력하세요. 오류로 멈추지 않고 `False`가 나와야 해요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w1d5.py`](../../exercises/week1/tests/test_w1d5.py)로 `is_valid_robot_id`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k is_valid_robot_id
   ```
   ✔ `9 passed, 10 deselected`가 나와야 해요.
5. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)를 여세요.
   `is_valid_robot_id` 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

### 연습 문제 4/4: `count_char(text, ch)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** `text` 안에 글자 `ch`가 몇 번 나오는지 세세요. `.count()` 대신 `for` 문을 사용하세요.

```python
>>> count_char("rail robot", "o")
2
```

**따라 해 볼 예제:** 비슷한 문제예요(이 연습 문제의 정답은 아니에요).

이 함수는 `for` 문으로 문자열을 한 글자씩 살펴보며 공백의 개수를 세요.

```python
def count_spaces(text):
    count = 0
    for ch in text:
        if ch == " ":
            count = count + 1
    return count
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과예요.

```python
$ python3 -i playground.py
>>> count_spaces('rail robot one')
2
>>> count_spaces('ROS')
0
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 편집기에서 [`exercises/week1/w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열려요. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d5_strings.py`](../../exercises/week1/w1d5_strings.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d5_strings.py`의 `count_char` 안에 있는 `pass`를 코드로 바꾸세요. 문자열을 반복문으로 살펴보고(5절) 누적 방법으로 개수를 세세요.
3. VS Code 편집기에서 **Ctrl + S**로 `w1d5_strings.py`를 저장하세요. 파일 탭의 **●**가 사라져요.

   VS Code 터미널에서 `python3 -i exercises/week1/w1d5_strings.py`를 실행하세요.
   **파이썬 `>>>` 프롬프트**에 위의 **할 일** 아래에 나온 `count_char(...)` 호출을 입력하고 결과를 비교하세요.

   `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
4. VS Code 터미널에서 [`test_w1d5.py`](../../exercises/week1/tests/test_w1d5.py)로 `count_char`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k count_char
   ```
   ✔ `4 passed, 15 deselected`가 나와야 해요.
5. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)를 여세요.
   `count_char` 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

### 마지막으로: 오늘의 테스트 전체와 이번 주 테스트 전체

VS Code 터미널에서 [`test_w1d5.py`](../../exercises/week1/tests/test_w1d5.py)의 오늘 테스트를 실행하세요.

```bash
pytest exercises/week1/tests/test_w1d5.py
```

✔ **`19 passed`**가 나와야 해요. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)의 5일차 "테스트 통과" 항목을 체크하세요. **Ctrl + S**로 저장하세요.

그런 다음 VS Code 터미널에서 [`exercises/week1/`](../../exercises/week1/)의 모든 테스트를 실행하세요.

```bash
pytest exercises/week1
```

✔ **`64 passed`**가 나와야 해요. 1–5일차의 모든 연습 문제예요.
VS Code 편집기에서 `progress/week1.md`의 "이번 주 전체 테스트 통과"를 체크하고 **Ctrl + S**로 저장하세요.

이전 연습 문제가 실패하면 VS Code 터미널 오류 메시지에 나온 파일을 고치고 **Ctrl + S**로 저장하세요.
주간 과제를 시작하기 전에 VS Code 터미널에서 `pytest exercises/week1`을 다시 실행하세요.

---

## 8. 주간 과제(오후)

VS Code 편집기에서 [checkpoints/week1/README.md](../../checkpoints/week1/README.md)를 열고 안내를 읽으세요. 안내에 따라 VS Code에서 [`checkpoints/week1/converter.py`](../../checkpoints/week1/converter.py)와 [`checkpoints/week1/guess.py`](../../checkpoints/week1/guess.py)를 작성하세요. 이번 주에 배운 내용을 모두 사용해요.

| 배운 내용 | 필요한 곳 |
|---|---|
| `print`, `:.2f`를 사용하는 f-문자열 | 메뉴와 결과 출력 |
| `input`, `int()`, `float()` | 사용자가 고른 항목과 입력값 읽기 |
| `return`을 사용하는 함수 | 변환 함수와 `check_guess` |
| `if` / `elif` / `else` | 할 일 고르기 |
| `while True` + `break` | `q`를 입력하거나 정답을 맞힐 때까지 반복 |
| `.isdigit()` | 추측한 값이 숫자인지 확인 |

주간 과제 파일 두 개를 모두 저장하세요. [`checkpoints/week1/`](../../checkpoints/week1/)의 테스트를 실행하세요(예상 결과: `11 passed`).

```bash
pytest checkpoints/week1
```

모든 테스트가 통과하면 VS Code 터미널에서 두 프로그램이 실행되는 모습을 **멘토에게 보여 주고** 코드를 설명하세요.

---

## 9. 1주차 완료

VS Code 편집기에서 [progress/week1.md](../../progress/week1.md)를 여세요. 완료한 **5일차**와 **1주차 완료** 항목을 `[x]`로 체크하세요.
**Ctrl + S**로 저장하세요.

- [ ] `pytest exercises/week1`의 테스트가 모두 통과해요
- [ ] `pytest checkpoints/week1`의 테스트가 모두 통과해요
- [ ] GitHub에서 최신 커밋에 ✅가 보여요
- [ ] 멘토에게 주간 과제가 동작하는 모습을 보여 줬어요
- [ ] 실습 일지 작성, 커밋, 푸시 완료

수고했어요! 다음 주에는 리스트, 딕셔너리, 함수의 더 자세한 내용, 파일에서 실제 센서 데이터를 읽는 방법을 배워요.
