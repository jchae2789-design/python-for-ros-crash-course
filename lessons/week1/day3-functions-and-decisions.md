# 1주차 · 3일차: 조건에 따라 판단하기, 함수와 `if` 문

**배울 내용:** 간단한 함수를 작성하는 방법, 값을 비교하는 방법, `if`, `elif`, `else`로 프로그램이 할 일을 고르게 하는 방법을 배워요.

**로봇을 다룰 때 필요한 이유:** 로봇은 계속 판단해요. *장애물이 너무 가까우면 멈춰요. 배터리가 부족하면 충전기로 돌아가요. 바람이 너무 강하면 이륙하지 않아요.* 모두 `if` 문으로 표현할 수 있어요.

---

## 1. 함수 처음 살펴보기

지금까지 프로그램은 위에서 아래로 한 번 실행됐어요. **함수**는 이름을 붙인 코드 묶음이에요. 원할 때마다 다른 값을 넣어 실행할 수 있어요.

```python
def double(number):
    result = number * 2
    return result


print(double(4))     # 8
print(double(10))    # 20
```

각 부분을 살펴보세요.

```python
def double(number):      # def는 함수를 정의한다는 뜻이에요. 함수 이름은 double이에요.
                         # number는 입력값을 받는 "매개변수"예요.
    result = number * 2  # 본문은 공백 4칸으로 들여써요
    return result        # return은 함수를 호출한 곳에 이 값을 돌려줘요
```

- `double(4)`는 함수를 **호출**해요. 함수 안에서 `number`는 `4`예요.
- `return`은 답을 돌려줘요. 그다음 `print(double(4))`가 그 답을 출력해요.

함수에는 여러 매개변수가 있을 수 있어요.

```python
def runtime_hours(capacity_mah, current_ma):
    return capacity_mah / current_ma


print(runtime_hours(5000, 2000))   # 2.5
```

### `return`과 `print`는 달라요

아주 중요한 차이예요.

- `print`는 화면에 값을 **보여 줘요**. 프로그램은 출력한 값을 이후 계산에 사용할 수 없어요.
- `return`은 값을 **돌려줘요**. 프로그램은 그 값을 저장하거나 계산에 사용하거나 출력할 수 있어요.

```python
def add_print(a, b):
    print(a + b)       # 화면에 보여 주고 값은 반환하지 않아요


def add_return(a, b):
    return a + b       # 값을 반환해요


x = add_return(2, 3)   # x는 5예요
y = add_print(2, 3)    # 5를 보여 주지만 y는 None(값이 없음)이에요
```

오늘부터 대부분의 연습 문제는 함수예요. 테스트가 함수를 호출해서 **반환하는 값**을 확인해요. 따라서 연습 문제 함수 안에서는 답을 `print`로 출력하지 말고 항상 `return`으로 반환하세요.

> 2주차에 함수를 더 자세히 배워요. 지금은 `def`, 매개변수, `return`만 알아도 충분해요.

---

## 2. 값 비교하기

비교 결과는 `True` 또는 `False`예요.

| 연산자 | 의미 | 예 | 결과 |
|---|---|---|---|
| `==` | 같아요 | `5 == 5` | `True` |
| `!=` | 달라요 | `5 != 3` | `True` |
| `<` | 작아요(미만) | `2 < 1` | `False` |
| `>` | 커요(초과) | `2 > 1` | `True` |
| `<=` | 작거나 같아요(이하) | `3 <= 3` | `True` |
| `>=` | 크거나 같아요(이상) | `4 >= 5` | `False` |

⚠️ `=`는 값을 저장해요. `==`는 두 값을 비교해요. 둘을 혼동하는 건 초보자가 가장 자주 하는 실수예요.

```python
battery = 20          # 저장해요
print(battery == 20)  # 비교해요 → True
```

---

## 3. `if`, `elif`, `else`

```python
distance = 0.3

if distance < 0.5:
    print("STOP!")
```

- `if` 뒤에는 조건과 콜론 `:`을 써요.
- `if`에 속하는 줄은 **공백 4칸으로 들여써요**. VS Code에서는 `:` 뒤에서 Enter를 누르면 자동으로 들여써 줘요.
- 조건이 `True`일 **때만** 이 줄들이 실행돼요.

### `else`: 그 밖의 경우

`playground.py`에서 이 예제 앞에 `distance = 0.3`을 두세요. `STOP!`이 나와야 해요.

```python
if distance < 0.5:
    print("STOP!")
else:
    print("Path is clear")
```

### `elif`: 조건을 더 추가하기

`elif`는 앞의 조건이 아니면 다음 조건을 확인한다는 뜻이에요. 파이썬은 **위에서 아래로** 조건을 확인하고 **처음으로 True가 되는 부분만** 실행해요.

```python
temperature = 65

if temperature >= 80:
    print("DANGER: shut down")
elif temperature >= 60:
    print("WARNING: too hot")
elif temperature >= 10:
    print("OK")
else:
    print("WARNING: too cold")
```

출력은 `WARNING: too hot`이에요. `65 >= 10`도 참이지만, 파이썬은 처음 맞는 조건을 찾으면 더 확인하지 않아요.

**순서가 중요해요!** `>= 10`을 먼저 쓰면 온도가 높은 경우에도 모두 `OK`가 출력돼요. 항상 가장 엄격한 조건부터 확인하세요.

### 함수 안의 `if` 문

```python
def temperature_status(temp):
    if temp >= 80:
        return "DANGER"
    elif temp >= 60:
        return "WARNING"
    else:
        return "OK"


print(temperature_status(85))   # DANGER
```

`return`이 실행되면 함수가 바로 끝나요.

---

## 4. 조건 조합하기: `and`, `or`, `not`

| 연산자 | 참이 되는 경우 | 예 |
|---|---|---|
| `and` | 양쪽 **모두** True일 때 | `battery > 20 and gps_ok` |
| `or` | **하나 이상**이 True일 때 | `emergency or battery < 5` |
| `not` | 반대 값 | `not gps_ok` |

```python
battery = 50
gps_ok = True
door_open = False

if battery > 20 and gps_ok and not door_open:
    print("Ready to move")
```

조건의 결과는 이미 `True` 또는 `False`이므로 바로 반환할 수 있어요.

```python
def is_hot(temp):
    return temp > 60     # True 또는 False를 반환해요


# 아래 코드도 같은 동작을 하지만 더 길어요.
def is_hot_long(temp):
    if temp > 60:
        return True
    else:
        return False
```

### 직접 해 보기

`playground.py`에 `needs_charging(battery, distance_to_dock)` 함수를 작성하세요. 배터리가 25 미만이면 `True`를 반환하세요.
배터리가 40 미만**이면서** 충전 지점까지 거리가 100 m를 초과할 때도 `True`를 반환하세요.

`playground.py`의 `needs_charging` 아래에 `print(needs_charging(20, 50))`을 추가하세요(예상 결과: `True`).
그런 다음 `print(needs_charging(50, 200))`을 추가하세요(예상 결과: `False`). **Ctrl + S**로 저장하고 VS Code 터미널에서 `python3 playground.py`를 실행하세요.

---

## 5. 들여쓰기

파이썬은 들여쓰기(줄 앞의 공백)로 어떤 줄들이 한 묶음인지 구분해요. **공백 4칸**을 사용하세요.
VS Code에서는 **Tab**을 누르면 공백 4칸이 들어가요.
아래 예제를 실행할 때는 `playground.py` 맨 앞에 `battery = 10`을 넣으세요. 세 줄이 모두 출력돼야 해요.

```python
if battery < 15:
    print("Battery critical")     # if 문 안에 있어요
    print("Returning to dock")    # if 문 안에 있어요
print("Check finished")           # 밖에 있으므로 항상 실행돼요
```

들여쓰기가 틀리면 `IndentationError`가 나요. 더 곤란한 경우에는 오류 없이 의도와 다르게 동작할 수도 있어요.

---

## 6. 자주 하는 실수

| 실수 | 해결 방법 |
|---|---|
| `if battery = 20:`에서 `SyntaxError`가 나와요 | 비교할 때는 `==`를 사용하세요 |
| `if`, `elif`, `else`, `def` 뒤에 `:`이 빠졌어요 | 콜론을 추가하세요 |
| 함수가 `None`을 반환해요 | `return` 대신 `print`를 사용했거나, 조건에 따라 실행되는 부분 중 한 곳에 `return`을 빠뜨렸어요 |
| 경계값(예: 정확히 90)에서 결과가 틀려요 | `>`와 `>=`를 확인하세요 |
| 모든 값이 첫 번째 조건에 걸려요 | `elif`의 순서를 확인하세요 |

---

## 7. 연습 문제

> 오늘부터 연습 문제는 **함수**예요. 먼저 [연습 문제 진행 방법 4부](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)를 읽으세요.

오늘의 함수는 모두 **한 파일**에 있어요. 한 번에 하나씩 작성하세요. 각 함수는 다음과 같이 진행해요.
- `pass`를 코드로 바꾸세요(`def ...` 줄은 그대로 두세요).
- `print` 대신 `return`으로 답을 반환하세요.
- 해당 연습 문제의 번호가 붙은 진행 순서에 나온 불러오기 명령, 함수 호출, `pytest` 명령을 따르세요.

**연습 문제 진행 방법:** 한 번에 하나씩 **순서대로** 푸세요. 아래의 각 연습 문제에는 번호가 붙은 진행 순서가 있어요. 1번부터 끝까지 따라 한 뒤 다음 연습 문제로 넘어가세요. 잘되지 않는 단계가 있으면 [연습 문제 진행 방법 5부](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 참고하세요.

세 함수는 모두 [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py)에 있어요. 아래에서 각 함수의 번호가 붙은 진행 순서를 따르세요.

### 연습 문제 1/3: `battery_status(percent)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 배터리 잔량에 맞는 상태 단어를 반환하세요.

| `percent` | 반환값 |
|---|---|
| 0 미만 또는 100 초과 | `"INVALID"` |
| 90 이상 | `"FULL"` |
| 40 이상 | `"OK"` |
| 15 이상 | `"LOW"` |
| 그보다 작은 값 | `"CRITICAL"` |

**따라 해 볼 예제:** 비슷한 문제예요(이 연습 문제의 정답은 아니에요).

이 함수는 Wi-Fi 신호 세기(dBm 단위이며 항상 0 이하)를 단어로 바꿔요. 잘못된 값인지 **먼저** 확인하고, 가장 엄격한 단계부터 약한 단계 순서로 확인한다는 점을 살펴보세요.

```python
def signal_quality(rssi):
    if rssi > 0:
        return "INVALID"
    elif rssi >= -50:
        return "EXCELLENT"
    elif rssi >= -70:
        return "GOOD"
    else:
        return "WEAK"
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과예요.

```python
$ python3 -i playground.py
>>> signal_quality(-45)
'EXCELLENT'
>>> signal_quality(-50)
'EXCELLENT'
>>> signal_quality(-80)
'WEAK'
>>> signal_quality(5)
'INVALID'
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열려요. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d3_conditions.py`의 `def battery_status(percent):`를 찾으세요.
3. VS Code 편집기에서 `w1d3_conditions.py`의 `battery_status` 안에 있는 `pass`를 알맞은 단어를 반환하는 `if` / `elif` / `else`로 바꾸세요. 조건을 확인하는 **순서**를 생각하세요(3절의 "`elif`: 조건을 더 추가하기").
4. VS Code 편집기에서 **Ctrl + S**로 `w1d3_conditions.py`를 저장하세요. 파일 탭의 **●**가 사라져요.
5. VS Code 터미널에 `w1d3_conditions.py`를 불러오는 아래 명령을 입력하세요. **파이썬 `>>>` 프롬프트**에 아래 함수 호출을 입력하세요. `>>>`가 없는 줄은 예상 결과예요.
   ```bash
   python3 -i exercises/week1/w1d3_conditions.py
   ```
   ```python
   >>> battery_status(55)
   'OK'
   >>> battery_status(90)
   'FULL'
   >>> battery_status(101)
   'INVALID'
   >>> exit()
   ```
   ✔ 표시된 답이 나와야 해요. 파일을 바꾸면 **Ctrl + S**로 저장하세요.
   파이썬이 아직 열려 있으면 `>>>`에 `exit()`을 입력하세요.
   저장한 코드를 사용하려면 위의 불러오기 명령을 다시 실행하세요.
6. VS Code 터미널에서 [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py)로 `battery_status`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d3.py -k battery_status
   ```
   ✔ `10 passed, 11 deselected`가 나와야 해요.
7. VS Code 편집기에서 [progress/week1.md](../../progress/week1.md)를 여세요.
   `battery_status` 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

> `deselected`는 이 파일에 있는 **다른** 연습 문제의 테스트는 실행하지 않았다는 뜻이에요. `-k`를 사용하면 이렇게 되니 괜찮아요.

### 연습 문제 2/3: `can_launch(battery_percent, wind_speed, gps_ok)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 드론이 이륙해도 되면 `True`, 아니면 `False`를 반환하세요. 배터리가 30 이상이고, 풍속이 8.0 이하이고, `gps_ok`가 `True`여야 해요. **세 조건 모두** 참이어야 해요.

**따라 해 볼 예제:** 비슷한 문제예요(이 연습 문제의 정답은 아니에요).

이 함수는 로봇이 주행해도 되는지 판단해요. 두 조건이 모두 참이어야 하므로 `and`로 연결하고, 결과(`True` 또는 `False`)를 바로 반환해요.

```python
def can_drive(speed, max_speed, emergency_stop):
    return speed <= max_speed and not emergency_stop
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과예요.

```python
$ python3 -i playground.py
>>> can_drive(1.0, 1.5, False)
True
>>> can_drive(1.5, 1.5, False)
True
>>> can_drive(2.0, 1.5, False)
False
>>> can_drive(1.0, 1.5, True)
False
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열려요. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d3_conditions.py`의 `def can_launch(...)`를 찾으세요.
3. VS Code 편집기에서 `w1d3_conditions.py`의 `can_launch` 안에 있는 `pass`를 코드로 바꾸세요. `and`를 사용하면 한 줄로 작성할 수 있어요(4절의 "바로 반환할 수 있어요" 참고).
4. VS Code 편집기에서 **Ctrl + S**로 `w1d3_conditions.py`를 저장하세요. 파일 탭의 **●**가 사라져요.
5. VS Code 터미널에 `python3 -i exercises/week1/w1d3_conditions.py`를 입력하세요. **파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. 나머지 줄은 예상 결과예요. 그런 다음 `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
   ```python
   >>> can_launch(80, 3.5, True)
   True
   >>> can_launch(80, 3.5, False)
   False
   ```
6. VS Code 터미널에서 [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py)로 `can_launch`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d3.py -k can_launch
   ```
   ✔ `5 passed, 16 deselected`가 나와야 해요.
7. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)를 여세요.
   `can_launch` 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

### 연습 문제 3/3: `classify_distance(distance_m)`

> 📖 **시작하기 전에:** [연습 문제 진행 방법](../../docs/02-how-exercises-work.md)을 이 수업 옆에 여세요.
> [4부: 함수 연습 문제](../../docs/02-how-exercises-work.md#4부-함수-연습-문제-따라-하기-35일차)와 [5부: 테스트 결과 읽기](../../docs/02-how-exercises-work.md#5부-테스트-결과-읽기)를 따라 하세요.

**할 일:** 로봇의 라이다가 장애물을 감지했어요. 거리가 0.5 m 미만이면 `"STOP"`, 2.0 m 미만이면 `"SLOW"`, 그 밖의 경우에는 `"GO"`를 반환하세요.

**따라 해 볼 예제:** 비슷한 문제예요(이 연습 문제의 정답은 아니에요).

이 함수는 연습 문제처럼 `<`를 사용해서 온도를 세 범위로 나눠요.

```python
def classify_temperature(temp_c):
    if temp_c < 0:
        return "FREEZING"
    elif temp_c < 30:
        return "NORMAL"
    else:
        return "HOT"
```

예제를 실행해 보세요. VS Code 터미널에 `code playground.py`를 입력해서 같은 VS Code 창에 `playground.py`를 여세요.
VS Code 편집기에서 `playground.py`에 예제를 입력하세요. **Ctrl + S**로 `playground.py`를 저장하세요.
VS Code 터미널에서 `python3 -i playground.py`를 실행하세요.

**파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. `>>>`가 없는 줄은 나와야 할 결과예요.

```python
$ python3 -i playground.py
>>> classify_temperature(-5)
'FREEZING'
>>> classify_temperature(0)
'NORMAL'
>>> classify_temperature(30)
'HOT'
>>> exit()
```

예제가 어떻게 동작하는지 이해했다면 아래 순서대로 진행하세요. 연습 문제 코드는 직접 작성하세요. 할 일이 다르니 예제를 그대로 복사하지 마세요.

**진행 순서:**

1. **파일을 여세요.** VS Code 편집기에서 **Ctrl + P**를 누르세요.
   VS Code 위쪽에 나타난 입력 칸에 [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py)를 입력하고 Enter를 누르세요. 편집기에 파일이 열려요. 또는 VS Code 편집기 왼쪽 파일 목록(**Explorer**)에서 [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py)를 클릭하세요.
2. VS Code 편집기에서 `w1d3_conditions.py`의 `def classify_distance(distance_m):`를 찾으세요.
3. VS Code 편집기에서 `w1d3_conditions.py`의 `classify_distance` 안에 있는 `pass`를 `if` / `elif` / `else`로 바꾸세요.
4. VS Code 편집기에서 **Ctrl + S**로 `w1d3_conditions.py`를 저장하세요. 파일 탭의 **●**가 사라져요.
5. VS Code 터미널에 `python3 -i exercises/week1/w1d3_conditions.py`를 입력하세요. **파이썬 `>>>` 프롬프트**에 아래 호출을 입력하세요. 나머지 줄은 예상 결과예요. 그런 다음 `>>>`에 `exit()`을 입력해서 VS Code 터미널로 돌아오세요.
   ```python
   >>> classify_distance(1.2)
   'SLOW'
   >>> classify_distance(0.5)
   'SLOW'
   ```
   정확히 0.5이면 0.5 미만이 **아니므로** `'STOP'`이 아니라 `'SLOW'`예요.
6. VS Code 터미널에서 [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py)로 `classify_distance`를 테스트하세요.
   ```bash
   pytest exercises/week1/tests/test_w1d3.py -k classify_distance
   ```
   ✔ `6 passed, 15 deselected`가 나와야 해요.
7. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)를 여세요.
   `classify_distance` 옆의 `[ ]`를 `[x]`로 바꾸고 **Ctrl + S**로 저장하세요.

### 마지막으로: 오늘의 테스트 전체

VS Code 터미널에서 [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py)의 오늘 테스트를 실행하세요.

```bash
pytest exercises/week1/tests/test_w1d3.py
```

✔ **`21 passed`**가 나와야 해요. VS Code 편집기에서 [`progress/week1.md`](../../progress/week1.md)의 3일차 "테스트 통과" 항목을 체크하세요. **Ctrl + S**로 저장하세요.

테스트는 정확히 `90`, `40`, `15`, `0.5`, `2.0`, `8.0` 같은 경계값을 사용해요. 한두 개만 실패한다면 `<`와 `<=`, `>`와 `>=`를 확인하세요.

---

## 8. 오늘 마치기 전에

VS Code 편집기에서 [progress/week1.md](../../progress/week1.md)를 여세요. 완료한 3일차 항목마다 `[x]`로 체크하세요.
**Ctrl + S**로 저장하세요. 3일차 항목을 모두 체크한 뒤에만 4일차를 시작하세요.

- [ ] `pytest exercises/week1/tests/test_w1d3.py` 실행 결과: **21 passed**
- [ ] `return`과 `print`의 차이를 설명할 수 있어요
- [ ] `=`와 `==`의 차이를 설명할 수 있어요
- [ ] 실습 일지 작성, 커밋, 푸시 완료

**다음:** [4일차: 반복하기, for 문과 while 문](day4-loops.md)
