# Week 1 · Day 5: Working with text + checkpoint

**You will learn:** how to get single characters and pieces out of a text, the most useful string methods, and how to loop over a text. In the afternoon you build the Week 1 checkpoint.

**Why this matters for robots:** ROS names everything with text: topics like `/rail_robot/lidar`, robot IDs, commands, log messages. You will check, clean and build these names all the time.

---

## 1. Indexing: one character

Every character in a string has a position number (**index**), starting at **0**:

```
 text:   R   R   -   0   0   4   2
 index:  0   1   2   3   4   5   6
 from end: -7  -6  -5  -4  -3  -2  -1
```

```python
robot_id = "RR-0042"
print(robot_id[0])     # R
print(robot_id[2])     # -
print(robot_id[-1])    # 2   (negative = count from the end)
print(len(robot_id))   # 7   (number of characters)
```

`robot_id[7]` gives `IndexError: string index out of range`. The last index is `len - 1`.

---

## 2. Slicing: a piece of the text

`text[start:stop]` gives the characters from `start` up to, **but not including**, `stop` (just like `range`):

```python
robot_id = "RR-0042"
print(robot_id[0:2])   # RR
print(robot_id[3:7])   # 0042
print(robot_id[3:])    # 0042   (no stop = until the end)
print(robot_id[:2])    # RR     (no start = from the beginning)
```

### Try it

For `topic = "/drone/camera"`, use slicing to get `drone` and `camera`.

---

## 3. String methods

A **method** is a function that belongs to a value. You call it with a dot: `text.method()`.

| Method | What it does | Example | Result |
|---|---|---|---|
| `.lower()` | all lowercase | `"LiDAR".lower()` | `"lidar"` |
| `.upper()` | all uppercase | `"stop".upper()` | `"STOP"` |
| `.strip()` | remove spaces/newlines at both ends | `"  go \n".strip()` | `"go"` |
| `.replace(a, b)` | replace every `a` with `b` | `"rail robot".replace(" ", "_")` | `"rail_robot"` |
| `.startswith(x)` | does it start with x? | `"/drone".startswith("/")` | `True` |
| `.endswith(x)` | does it end with x? | `"scan.csv".endswith(".csv")` | `True` |
| `.isdigit()` | only digits 0–9? | `"0042".isdigit()` | `True` |
| `.isalpha()` | only letters? | `"RR".isalpha()` | `True` |
| `.isupper()` | all letters uppercase? | `"RR".isupper()` | `True` |

Important: strings **cannot be changed**. Methods give back a **new** string. Store it:

```python
command = "  FORWARD  "
command.strip()             # does nothing to command!
command = command.strip()   # ✅ store the new string
```

You can **chain** methods. They run from left to right:

```python
"  Turn LEFT  ".strip().lower()     # "turn left"
```

### Joining strings

`+` glues strings together:

```python
robot = "drone"
topic = "/" + robot + "/camera"     # "/drone/camera"
```

An f-string often reads better: `f"/{robot}/camera"`.

---

## 4. `in`: does it contain…?

```python
print("lidar" in "/rail_robot/lidar")    # True
print("x" in "robot")                    # False
```

---

## 5. Looping over a string

A `for` loop can go through a string, one character at a time:

```python
for ch in "ROS":
    print(ch)
```

```
R
O
S
```

Combined with the accumulator pattern from Day 4:

```python
digits = 0
for ch in "RR-0042":
    if ch.isdigit():
        digits = digits + 1
print(digits)       # 4
```

---

## 6. Common mistakes

| Mistake | Fix |
|---|---|
| `text.lower()` "does not work" | Store the result: `text = text.lower()` |
| `IndexError: string index out of range` | The last index is `len(text) - 1` |
| `text[0:2]` gives 2 characters, not 3 | The stop index is not included |
| `"robot".upper` prints `<built-in method ...>` | Methods need brackets: `.upper()` |

---

## 7. Exercises (morning)

Open `exercises/week1/w1d5_strings.py`. There are four functions.

For `is_valid_robot_id`, check the length **first**. If the text is too short, `robot_id[2]` would crash.

```bash
pytest exercises/week1/tests/test_w1d5.py
```

Then check the **whole week**:

```bash
pytest exercises/week1
```

---

## 8. Checkpoint (afternoon)

Read [checkpoints/week1/README.md](../../checkpoints/week1/README.md) and build the two programs. They use everything from this week:

| Skill | Where you need it |
|---|---|
| `print`, f-strings with `:.2f` | the menu and the results |
| `input`, `int()`, `float()` | reading the user's choice and values |
| functions with `return` | the converters and `check_guess` |
| `if` / `elif` / `else` | choosing what to do |
| `while True` + `break` | repeating until `q` or the correct guess |
| `.isdigit()` | checking if a guess is a number |

```bash
pytest checkpoints/week1
```

When all tests pass, **show your mentor** both programs running in the terminal and explain your code.

---

## 9. Week 1 finished

Check off **Day 5** and **Week 1 done** in your checklist: [progress/week1.md](../../progress/week1.md).

- [ ] `pytest exercises/week1` passes completely
- [ ] `pytest checkpoints/week1` passes completely
- [ ] On GitHub, my latest commit shows ✅
- [ ] I demonstrated the checkpoint to my mentor
- [ ] Daily log written, committed and pushed

Well done! Next week: lists, dictionaries, more about functions, and reading real sensor data from files.
