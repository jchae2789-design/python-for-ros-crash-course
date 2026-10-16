# Week 1 · Day 2: Variables, numbers and input

**You will learn:** how to store values in variables, the main data types, math in Python, how to ask the user for input, and how to format numbers nicely.

**Why this matters for robots:** a robot is full of numbers: distance from a LiDAR, battery voltage, wheel speed, angle. Your code stores them in variables, calculates with them and shows them to people.

---

## 1. Variables

A **variable** is a name for a value. Think of it as a labeled box.

```python
speed = 0.5
robot_name = "RR-01"
battery = 87

print(robot_name)
print(speed)
```

`=` means **"store the value on the right in the name on the left"**. It does not mean "is equal" like in math.

You can change a variable later:

```python
battery = 87
battery = battery - 10    # take the old value, subtract 10, store it again
print(battery)            # 77
```

### Naming rules

- Use lowercase letters, digits and `_`. Write words with `_` between them: `wheel_speed`, `max_distance`. This style is called **snake_case**, and ROS uses it everywhere.
- A name cannot start with a digit: `1st_robot` ❌, `robot_1` ✅
- Names are case-sensitive: `Speed` and `speed` are two different variables.
- Choose names that explain the value: `distance_m` is better than `d` or `x`.

---

## 2. Data types

Every value has a **type**:

| Type | Name | Examples | Used for |
|---|---|---|---|
| `int` | integer (whole number) | `7`, `-3`, `5000` | counts, IDs, battery % |
| `float` | decimal number | `0.5`, `3.14`, `-2.0` | distances, speeds, angles |
| `str` | string (text) | `"RR-01"`, `'hello'` | names, messages, commands |
| `bool` | boolean (true/false) | `True`, `False` | "is the GPS OK?" |

At Python's `>>>` prompt, type the `type(...)` calls below to see each value's type:

```python
>>> type(7)
<class 'int'>
>>> type(0.5)
<class 'float'>
>>> type("7")
<class 'str'>
```

Careful: `7` and `"7"` are **different**. `7` is a number. `"7"` is text that looks like a number.

---

## 3. Math

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide (always gives a float) | `7 / 2` | `3.5` |
| `//` | whole-number division | `7 // 2` | `3` |
| `%` | remainder (modulo) | `7 % 2` | `1` |
| `**` | power | `2 ** 3` | `8` |

Python follows math rules: `*` and `/` before `+` and `-`. Use brackets to be clear:

```python
average = (10 + 20) / 2     # 15.0
```

### `//` and `%` together

They are very useful for splitting things into units. 135 minutes = how many hours and minutes?

```python
total = 135
hours = total // 60      # 2  (how many full hours)
minutes = total % 60     # 15 (what is left over)
```

### The `math` module

Python has extra math tools in the `math` module. In `playground.py` in VS Code, put `import math` before the calls to `math.pi` and `math.sqrt`:

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
```

ROS measures angles in **radians**, not degrees, so you will see `math.pi` a lot.

### Try it

In the VS Code terminal, type `python3`. At Python's `>>>` prompt, calculate the following values; then type `exit()` to return to the VS Code terminal:
1. How many full minutes are in 500 seconds, and how many seconds are left?
2. A robot drives at 0.4 m/s for 90 seconds. How far does it go?
3. The square root of 2 (first type `import math` at `>>>`).

---

## 4. Converting types

Sometimes you need to change a value from one type to another. Run `python3`.
At Python's **`>>>` prompt**, type each call below. The comments show the results.

Type `exit()` at `>>>` when finished:

```python
int("42")       # 42     text → whole number
float("3.5")    # 3.5    text → decimal number
str(42)         # "42"   number → text
int(3.9)        # 3      cuts off the decimals (does not round!)
round(3.9)      # 4      rounds
round(3.14159, 2)  # 3.14
```

If the text is not a number, you get an error:

```python
>>> int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
```

---

## 5. Asking the user: `input()`

`input()` shows a message, waits for the user to type something and press Enter, and gives back what they typed.

```python
name = input("Robot name: ")
print("Starting", name)
```

```
Robot name: RR-01
Starting RR-01
```

⚠️ **`input()` always gives back a `str`**, even when the user types a number:

```python
distance = input("Distance (m): ")    # user types 10
print(distance * 2)                   # 1010  ← text repeated twice!
```

In `playground.py`, replace the distance example with the version below. It converts the input to `float`. Save with **Ctrl + S**. Run `python3 playground.py` in the VS Code terminal. At `Distance (m):`, type `10` and press Enter:

```python
distance = float(input("Distance (m): "))
print(distance * 2)                   # 20.0 ✅
```

---

## 6. f-strings: putting values into text

An **f-string** starts with `f` before the quote. Inside, you put variables in `{ }`:

```python
robot = "RR-01"
battery = 87
print(f"Robot {robot} has {battery}% battery")
```

```
Robot RR-01 has 87% battery
```

### Number formatting

Add `:.2f` after a value to show exactly 2 decimals:

```python
voltage = 12.34567
print(f"Voltage: {voltage:.2f} V")     # Voltage: 12.35 V
print(f"Voltage: {voltage:.1f} V")     # Voltage: 12.3 V
print(f"Distance: {5:.2f} m")          # Distance: 5.00 m
```

You will use f-strings in almost every program, including ROS log messages.

### Try it

In `playground.py`, write a program that asks for speed in m/s. Print the speed in km/h with 1 decimal. Save with **Ctrl + S**. Run `python3 playground.py` in the VS Code terminal.

At `Speed (m/s):`, type `2.5` and press Enter. Expect the result below. (1 m/s = 3.6 km/h.)

```
Speed (m/s): 2.5
2.5 m/s = 9.0 km/h
```

---

## 7. Common mistakes

| Mistake | Fix |
|---|---|
| `"5" + 3` gives `TypeError: can only concatenate str (not "int") to str` | Convert first: `int("5") + 3` |
| Calculating with `input()` gives strange results | Wrap it: `int(input(...))` or `float(input(...))` |
| `print("Battery: {battery}")` prints `{battery}` literally | You forgot the `f`: `print(f"Battery: {battery}")` |
| `Speed = 1` then `print(speed)` gives `NameError` | Names are case-sensitive |

---

## 8. Exercises

**How to do the exercises:** do them **in order**, one at a time. Each exercise below has numbered steps. Follow them from 1 to the end, then go to the next exercise. If a step does not work, look at [How exercises work, Part 5](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

### Exercise 1 of 2: Battery runtime

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 3: a script exercise](../../docs/02-how-exercises-work.md#part-3-worked-example-a-script-exercise-days-12) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** ask for a battery's capacity (mAh) and the current the robot uses (mA). Print how many hours the battery lasts: capacity ÷ current, with 2 decimals.

**What it should look like** (you type `5000` and `2000`):

```
$ python3 exercises/week1/w1d2_battery_runtime.py
Capacity (mAh): 5000
Current (mA): 2000
Runtime: 2.50 hours
```

**Example to follow:** a similar problem (not the answer to this exercise).

This program asks for a distance and a speed, and prints how long the trip takes. It uses the same three parts as your exercise: two `input()` calls with `int()`, one division, and one f-string with `:.2f`.

```python
distance = int(input("Distance (m): "))
speed = int(input("Speed (m/min): "))
travel_time = distance / speed
print(f"Travel time: {travel_time:.2f} minutes")
```

Try the example: in the VS Code terminal, type `code playground.py` to open `playground.py` in the same VS Code window.
In the VS Code editor, type the example into `playground.py`. Save `playground.py` with **Ctrl + S**.
Run `python3 playground.py` in the VS Code terminal.

When it asks, type `100`, press Enter, type `40`, press Enter:

```
$ python3 playground.py
Distance (m): 100
Speed (m/min): 40
Travel time: 2.50 minutes
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In the VS Code editor, press **Ctrl + P**.
   Type [`exercises/week1/w1d2_battery_runtime.py`](../../exercises/week1/w1d2_battery_runtime.py) and press Enter. The file opens in the editor. Or click [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d2_battery_runtime.py`](../../exercises/week1/w1d2_battery_runtime.py) in the file list on the left (Explorer) in the VS Code editor.
2. In the VS Code editor, in `w1d2_battery_runtime.py`, read the instructions at the top of the file.
3. In the VS Code editor, in `w1d2_battery_runtime.py`, write your code below `TODO`. You need:
   - two `input()` calls, each wrapped in `int()` (section 5 of this lesson),
   - one division,
   - one `print()` with an f-string and `:.2f` (section 6).
4. In the VS Code editor, save `w1d2_battery_runtime.py` with **Ctrl + S**. The **●** on the file's tab disappears when it is saved.
5. In the VS Code terminal, run `w1d2_battery_runtime.py`. At `Capacity (mAh):`, type `5000` and press Enter. Then at `Current (mA):`, type `2000` and press Enter:
   ```bash
   python3 exercises/week1/w1d2_battery_runtime.py
   ```
   ✔ The last line should be `Runtime: 2.50 hours`. Run `python3 exercises/week1/w1d2_battery_runtime.py` again. Enter `1000` at `Capacity (mAh):`.
   Enter `3000` at `Current (mA):`. Press Enter after each value. That should give `Runtime: 0.33 hours`.
   ✘ If **nothing appears at all**, your file has no code yet or is not saved. Go back to step 3.
6. In the VS Code terminal, test `w1d2_battery_runtime.py` with [`test_w1d2.py`](../../exercises/week1/tests/test_w1d2.py):
   ```bash
   pytest exercises/week1/tests/test_w1d2.py -k battery
   ```
   ✔ You should see `3 passed, 3 deselected`. The test runs your program 3 times with different numbers.
7. In the VS Code editor, open [progress/week1.md](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `exercises/week1/w1d2_battery_runtime.py`. Save with **Ctrl + S**.

> `deselected` means: the tests of the **other** exercises in this file were not run. That is what `-k` does, and it is fine.

### Exercise 2 of 2: Mission timer

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 3: a script exercise](../../docs/02-how-exercises-work.md#part-3-worked-example-a-script-exercise-days-12) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** ask for a number of seconds. Print it as hours, minutes and seconds.

**What it should look like** (you type `3725`):

```
$ python3 exercises/week1/w1d2_time_format.py
Seconds: 3725
1 h 2 m 5 s
```

**Example to follow:** a similar problem (not the answer to this exercise).

This program splits a length in centimeters into meters and centimeters, with `//` and `%`. Your exercise has **three** units (hours, minutes, seconds), so you need one more step.

```python
total_cm = int(input("Length (cm): "))
meters = total_cm // 100
cm = total_cm % 100
print(f"{meters} m {cm} cm")
```

Try the example: in the VS Code terminal, type `code playground.py` to open `playground.py` in the same VS Code window.
In the VS Code editor, type the example into `playground.py`. Save `playground.py` with **Ctrl + S**.
Run `python3 playground.py` in the VS Code terminal.

When it asks, type `275` and press Enter:

```
$ python3 playground.py
Length (cm): 275
2 m 75 cm
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In the VS Code editor, press **Ctrl + P**.
   Type [`exercises/week1/w1d2_time_format.py`](../../exercises/week1/w1d2_time_format.py) and press Enter. The file opens in the editor. Or click [`exercises`](../../exercises/) → [`week1`](../../exercises/week1/) → [`w1d2_time_format.py`](../../exercises/week1/w1d2_time_format.py) in the file list on the left (Explorer) in the VS Code editor.
2. In the VS Code editor, in `w1d2_time_format.py`, read the instructions at the top of the file.
3. In the VS Code editor, in `w1d2_time_format.py`, write your code below `TODO`. Use `//` and `%` (section 3 of this lesson, "`//` and `%` together"). There are 3600 seconds in an hour and 60 in a minute.
   Tip: first work it out on paper for 3725: how many full hours? How many seconds are left? How many full minutes in those?
4. In the VS Code editor, save `w1d2_time_format.py` with **Ctrl + S**. The **●** on the file's tab disappears when it is saved.
5. In the VS Code terminal, run `w1d2_time_format.py`. At `Seconds:`, type `3725` and press Enter:
   ```bash
   python3 exercises/week1/w1d2_time_format.py
   ```
   ✔ You should see `1 h 2 m 5 s`. Run `python3 exercises/week1/w1d2_time_format.py` again. Enter `59` at `Seconds:` (→ `0 h 0 m 59 s`). Then run the same command again. Enter `7200` at `Seconds:` (→ `2 h 0 m 0 s`), pressing Enter after each value.
   ✘ If **nothing appears at all**, your file has no code yet or is not saved. Go back to step 3.
6. In the VS Code terminal, test `w1d2_time_format.py` with [`test_w1d2.py`](../../exercises/week1/tests/test_w1d2.py):
   ```bash
   pytest exercises/week1/tests/test_w1d2.py -k time_format
   ```
   ✔ You should see `3 passed, 3 deselected`.
7. In the VS Code editor, open [`progress/week1.md`](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `w1d2_time_format.py`. Save with **Ctrl + S**.

### Finally: all of today's tests

In the VS Code terminal, run today's tests in [`test_w1d2.py`](../../exercises/week1/tests/test_w1d2.py):

```bash
pytest exercises/week1/tests/test_w1d2.py
```

✔ You should see **`6 passed`**. In the VS Code editor, check the Day 2 "Tests pass" box in [`progress/week1.md`](../../progress/week1.md). Save with **Ctrl + S**.

---

## 9. Before you finish today

In the VS Code editor, open [progress/week1.md](../../progress/week1.md). Mark each completed Day 2 box `[x]`.
Save with **Ctrl + S**. Only start Day 3 when every Day 2 box is checked.

- [ ] `pytest exercises/week1/tests/test_w1d2.py` shows **6 passed**
- [ ] I can explain the difference between `7`, `7.0` and `"7"`
- [ ] I can explain what `//` and `%` do
- [ ] Daily log written, committed and pushed

**Next:** [Day 3: Making decisions: functions and if](day3-functions-and-decisions.md)
