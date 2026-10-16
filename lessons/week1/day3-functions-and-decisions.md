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

Write a function `needs_charging(battery, distance_to_dock)` that returns `True` if the battery is below 25, **or** if the battery is below 40 **and** the dock is more than 100 m away. Test it with a few calls and `print()`.

---

## 5. Indentation

Python uses indentation (spaces at the start of a line) to know which lines belong together. Use **4 spaces**. VS Code inserts them when you press **Tab**.

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

Open `exercises/week1/w1d3_conditions.py`. It has three functions. Replace `pass` with your code.

To check your work by hand, load your file in interactive mode and call your functions:

```bash
python3 -i exercises/week1/w1d3_conditions.py
```

```python
>>> battery_status(55)
'OK'
>>> exit()
```

Then run the tests:

```bash
pytest exercises/week1/tests/test_w1d3.py
```

Look closely at the edge values in the tests: `90`, `40`, `15`, `0.5`, `2.0`, `8.0`. They check whether you used `<` or `<=` correctly.

---

## 8. Before you finish today

- [ ] `pytest exercises/week1/tests/test_w1d3.py` shows **21 passed**
- [ ] I can explain the difference between `return` and `print`
- [ ] I can explain the difference between `=` and `==`
- [ ] Daily log written, committed and pushed

**Next:** [Day 4: Repeating: for and while loops](day4-loops.md)
