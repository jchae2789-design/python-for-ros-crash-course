# Week 1 · Day 3: Making decisions: functions and `if`

**You will learn:** how to write a simple function, how to compare values, and how to make your program choose what to do with `if`, `elif` and `else`.

**Why this matters for robots:** robots decide all the time. *Is the obstacle too close? Stop. Is the battery low? Go back to the charger. Is the wind too strong? Do not take off.* This is all `if`.

---

## 1. A first look at functions

Until now, your programs ran from top to bottom once. A **function** is a named piece of code that you can run whenever you want, with different values.

```python
def double(number):
    result = number * 2
    return result


print(double(4))     # 8
print(double(10))    # 20
```

The parts:

```python
def double(number):      # def = "define a function". Its name is double.
                         # number is the input (a "parameter").
    result = number * 2  # the body: indented by 4 spaces
    return result        # return = give this value back to whoever called the function
```

- `double(4)` **calls** the function. Inside, `number` is `4`.
- `return` sends the answer back. `print(double(4))` then prints it.

A function can have several parameters:

```python
def runtime_hours(capacity_mah, current_ma):
    return capacity_mah / current_ma


print(runtime_hours(5000, 2000))   # 2.5
```

### `return` is not `print`

This is very important:

- `print` **shows** a value on the screen. The program cannot use it afterwards.
- `return` **gives back** a value. The program can store it, calculate with it, or print it.

```python
def add_print(a, b):
    print(a + b)       # shows it, gives back nothing


def add_return(a, b):
    return a + b       # gives it back


x = add_return(2, 3)   # x is 5
y = add_print(2, 3)    # shows 5, but y is None (nothing)
```

From today on, most exercises are functions. The tests call your function and check what it **returns**. So always use `return`, not `print`, inside exercise functions.

> You will learn much more about functions in Week 2. For now, this is enough: `def`, parameters, `return`.

---

## 2. Comparing values

A comparison gives back `True` or `False`:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal | `5 == 5` | `True` |
| `!=` | not equal | `5 != 3` | `True` |
| `<` | less than | `2 < 1` | `False` |
| `>` | greater than | `2 > 1` | `True` |
| `<=` | less than or equal | `3 <= 3` | `True` |
| `>=` | greater than or equal | `4 >= 5` | `False` |

⚠️ `=` stores a value. `==` compares two values. Mixing them up is the most common beginner mistake.

```python
battery = 20          # store
print(battery == 20)  # compare → True
```

---

## 3. `if`, `elif`, `else`

```python
distance = 0.3

if distance < 0.5:
    print("STOP!")
```

- After `if` comes a condition and a colon `:`.
- The lines that belong to the `if` are **indented by 4 spaces**. VS Code does this for you when you press Enter after `:`.
- They run **only if** the condition is `True`.

### `else`: otherwise

Keep `distance = 0.3` before this example in `playground.py`; expect `STOP!`.

```python
if distance < 0.5:
    print("STOP!")
else:
    print("Path is clear")
```

### `elif`: more choices

`elif` means "else if". Python checks the conditions **from top to bottom** and runs **only the first one that is True**:

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

Output: `WARNING: too hot`. Even though `65 >= 10` is also true, Python stops after the first match.

**The order matters!** If you put `>= 10` first, every warm temperature would print `OK`. Always put the strictest check first.

### `if` inside a function

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

When `return` runs, the function stops immediately.

---

## 4. Combining conditions: `and`, `or`, `not`

| Operator | True when | Example |
|---|---|---|
| `and` | **both** sides are True | `battery > 20 and gps_ok` |
| `or` | **at least one** side is True | `emergency or battery < 5` |
| `not` | the opposite | `not gps_ok` |

```python
battery = 50
gps_ok = True
door_open = False

if battery > 20 and gps_ok and not door_open:
    print("Ready to move")
```

A condition is already `True` or `False`, so you can return it directly:

```python
def is_hot(temp):
    return temp > 60     # gives back True or False


# This is the same, but longer:
def is_hot_long(temp):
    if temp > 60:
        return True
    else:
        return False
```

### Try it

In `playground.py`, write a function `needs_charging(battery, distance_to_dock)`. Return `True` if the battery is below 25.
Also return `True` if the battery is below 40 **and** the dock is more than 100 m away.

Below `needs_charging` in `playground.py`, add `print(needs_charging(20, 50))` (expected: `True`).
Then add `print(needs_charging(50, 200))` (expected: `False`). Save with **Ctrl + S**. Run `python3 playground.py` in the terminal.

---

## 5. Indentation

Python uses indentation (spaces at the start of a line) to know which lines belong together. Use **4 spaces**.
VS Code inserts four spaces when you press **Tab**.
For the example below, put `battery = 10` first in `playground.py`; the three print lines should appear.

```python
if battery < 15:
    print("Battery critical")     # inside the if
    print("Returning to dock")    # inside the if
print("Check finished")           # outside: always runs
```

Wrong indentation gives `IndentationError`, or worse: no error, but the wrong behavior.

---

## 6. Common mistakes

| Mistake | Fix |
|---|---|
| `if battery = 20:` gives `SyntaxError` | Use `==` to compare |
| Missing `:` after `if`, `elif`, `else` or `def` | Add the colon |
| The function returns `None` | You used `print` instead of `return`, or forgot `return` in one branch |
| Wrong result for the edge values (e.g. exactly 90) | Check `>` vs `>=` |
| Every value goes into the first branch | Check the order of your `elif`s |

---

## 7. Exercises

> From today, exercises are **functions**. Read [How exercises work, Part 4](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) first.

All of today's functions are in **one file**. You write them one at a time. For each function, you:
- replace `pass` with your code (keep the `def ...` line exactly as it is),
- use `return` to give back the answer (not `print`),
- follow the load command, function calls, and `pytest` command in that exercise's numbered steps.

**How to do the exercises:** do them **in order**, one at a time. Each exercise below has numbered steps. Follow them from 1 to the end, then go to the next exercise. If a step does not work, look at [How exercises work, Part 5](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

All three functions are in [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py). Follow the numbered steps for each function below.

### Exercise 1 of 3: `battery_status(percent)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** return a status word for a battery level:

| `percent` | return |
|---|---|
| below 0 or above 100 | `"INVALID"` |
| 90 or more | `"FULL"` |
| 40 or more | `"OK"` |
| 15 or more | `"LOW"` |
| anything lower | `"CRITICAL"` |

**Example to follow:** a similar problem (not the answer to this exercise).

This function turns a Wi-Fi signal strength (in dBm, always 0 or below) into a word. Notice: the invalid check comes **first**, then the strictest level, then weaker ones.

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

Try the example: open `playground.py` with `code playground.py`.
Type the example in VS Code. Save with **Ctrl + S**.
Run `python3 -i playground.py` in the terminal.

At `>>>`, type the calls below. The lines without `>>>` are the results you should see:

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

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, press **Ctrl + P**.
   Type [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py) and press Enter. The file opens in the editor.
2. Find `def battery_status(percent):`.
3. Replace `pass` inside `battery_status` with an `if` / `elif` / `else` that returns the right word. Think about the **order** of your checks (section 3, "`elif`: more choices").
4. Save with **Ctrl + S**. The **●** on the file tab disappears.
5. In the terminal, type the command below. At `>>>`, type the function calls below. The lines without `>>>` show the expected results:
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
   ✔ You should get the answers shown. After changing the file, save with **Ctrl + S**.
   If Python is still open, type `exit()` at `>>>`.
   Repeat the load command above to use the saved code.
6. Test `battery_status` with [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py):
   ```bash
   pytest exercises/week1/tests/test_w1d3.py -k battery_status
   ```
   ✔ You should see `10 passed, 11 deselected`.
7. In VS Code, open [progress/week1.md](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `battery_status`. Save with **Ctrl + S**.

> `deselected` means: the tests of the **other** exercises in this file were not run. That is what `-k` does, and it is fine.

### Exercise 2 of 3: `can_launch(battery_percent, wind_speed, gps_ok)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** return `True` if a drone may take off, otherwise `False`. **All three** must be true: battery is 30 or more, wind is 8.0 or less, and `gps_ok` is `True`.

**Example to follow:** a similar problem (not the answer to this exercise).

This function decides if a robot may drive. Both conditions must be true, so they are joined with `and`, and the result (`True` or `False`) is returned directly:

```python
def can_drive(speed, max_speed, emergency_stop):
    return speed <= max_speed and not emergency_stop
```

Try the example: open `playground.py` with `code playground.py`.
Type the example in VS Code. Save with **Ctrl + S**.
Run `python3 -i playground.py` in the terminal.

At `>>>`, type the calls below. The lines without `>>>` are the results you should see:

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

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, press **Ctrl + P**.
   Type [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py) and press Enter. The file opens in the editor.
2. Find `def can_launch(...)` in the file.
3. Replace `pass` inside `can_launch` with your code. You can do it in one line with `and` (section 4: "you can return it directly").
4. Save with **Ctrl + S**. The **●** on the file tab disappears.
5. In the terminal, type `python3 -i exercises/week1/w1d3_conditions.py`. At `>>>`, type the calls below. The other lines show the expected results. Then type `exit()` at `>>>` to return to the terminal:
   ```python
   >>> can_launch(80, 3.5, True)
   True
   >>> can_launch(80, 3.5, False)
   False
   ```
6. Test `can_launch` with [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py):
   ```bash
   pytest exercises/week1/tests/test_w1d3.py -k can_launch
   ```
   ✔ You should see `5 passed, 16 deselected`.
7. In VS Code, open [`progress/week1.md`](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `can_launch`. Save with **Ctrl + S**.

### Exercise 3 of 3: `classify_distance(distance_m)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** a robot's LiDAR sees an obstacle. Return `"STOP"` if it is closer than 0.5 m, `"SLOW"` if it is closer than 2.0 m, otherwise `"GO"`.

**Example to follow:** a similar problem (not the answer to this exercise).

This function sorts a temperature into three groups, using `<` like your exercise:

```python
def classify_temperature(temp_c):
    if temp_c < 0:
        return "FREEZING"
    elif temp_c < 30:
        return "NORMAL"
    else:
        return "HOT"
```

Try the example: open `playground.py` with `code playground.py`.
Type the example in VS Code. Save with **Ctrl + S**.
Run `python3 -i playground.py` in the terminal.

At `>>>`, type the calls below. The lines without `>>>` are the results you should see:

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

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, press **Ctrl + P**.
   Type [`exercises/week1/w1d3_conditions.py`](../../exercises/week1/w1d3_conditions.py) and press Enter. The file opens in the editor.
2. Find `def classify_distance(distance_m):` in the file.
3. Replace `pass` inside `classify_distance` with an `if` / `elif` / `else`.
4. Save with **Ctrl + S**. The **●** on the file tab disappears.
5. In the terminal, type `python3 -i exercises/week1/w1d3_conditions.py`. At `>>>`, type the calls below. The other lines show the expected results. Then type `exit()` at `>>>` to return to the terminal:
   ```python
   >>> classify_distance(1.2)
   'SLOW'
   >>> classify_distance(0.5)
   'SLOW'
   ```
   Exactly 0.5 is **not** closer than 0.5, so it is `'SLOW'`, not `'STOP'`.
6. Test `classify_distance` with [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py):
   ```bash
   pytest exercises/week1/tests/test_w1d3.py -k classify_distance
   ```
   ✔ You should see `6 passed, 15 deselected`.
7. In VS Code, open [`progress/week1.md`](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `classify_distance`. Save with **Ctrl + S**.

### Finally: all of today's tests

Run today's tests in [`test_w1d3.py`](../../exercises/week1/tests/test_w1d3.py):

```bash
pytest exercises/week1/tests/test_w1d3.py
```

✔ You should see **`21 passed`**. In VS Code, check the Day 3 "Tests pass" box in [`progress/week1.md`](../../progress/week1.md). Save with **Ctrl + S**.

The tests use edge values like exactly `90`, `40`, `15`, `0.5`, `2.0` and `8.0`. If only one or two tests fail, check `<` vs `<=` and `>` vs `>=`.

---

## 8. Before you finish today

In VS Code, open [progress/week1.md](../../progress/week1.md). Mark each completed Day 3 box `[x]`.
Save with **Ctrl + S**. Only start Day 4 when every Day 3 box is checked.

- [ ] `pytest exercises/week1/tests/test_w1d3.py` shows **21 passed**
- [ ] I can explain the difference between `return` and `print`
- [ ] I can explain the difference between `=` and `==`
- [ ] Daily log written, committed and pushed

**Next:** [Day 4: Repeating: for and while loops](day4-loops.md)
