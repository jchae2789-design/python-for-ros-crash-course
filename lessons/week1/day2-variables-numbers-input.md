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

Check a type with `type()`:

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

Python has extra math tools in the `math` module. You must **import** it first:

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
```

ROS measures angles in **radians**, not degrees, so you will see `math.pi` a lot.

### Try it

In `python3`, calculate:
1. How many full minutes are in 500 seconds, and how many seconds are left?
2. A robot drives at 0.4 m/s for 90 seconds. How far does it go?
3. The square root of 2.

---

## 4. Converting types

Sometimes you need to change a value from one type to another:

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

Convert it first:

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

Write a small program that asks for a speed in m/s and prints it in km/h with 1 decimal. (1 m/s = 3.6 km/h.)

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

1. `exercises/week1/w1d2_battery_runtime.py`
2. `exercises/week1/w1d2_time_format.py`

Run your program and type the example values yourself:

```bash
python3 exercises/week1/w1d2_battery_runtime.py
```

Then test:

```bash
pytest exercises/week1/tests/test_w1d2.py
```

---

## 9. Before you finish today

Check off **Day 2** in your checklist: [progress/week1.md](../../progress/week1.md). Only start Day 3 when every Day 2 box is checked.

- [ ] `pytest exercises/week1/tests/test_w1d2.py` shows **6 passed**
- [ ] I can explain the difference between `7`, `7.0` and `"7"`
- [ ] I can explain what `//` and `%` do
- [ ] Daily log written, committed and pushed

**Next:** [Day 3: Making decisions: functions and if](day3-functions-and-decisions.md)
