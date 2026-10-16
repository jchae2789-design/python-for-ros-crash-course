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

**How to do the exercises:** do them **in order**, one at a time. Each exercise below has numbered steps. Follow them from 1 to the end, then go to the next exercise. If a step does not work, look at [How exercises work, Part 5](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

All four functions are in `exercises/week1/w1d5_strings.py`. Open it in VS Code now. For each one: replace `pass`, save, try it with `python3 -i exercises/week1/w1d5_strings.py`, run its tests, then check its box in [progress/week1.md](../../progress/week1.md).

### Exercise 1 of 4: `clean_command(text)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson and follow it while you do this exercise, especially [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** remove spaces and newlines at both ends, and make the text lowercase.

```python
>>> clean_command("  FORWARD \n")
'forward'
```

**Example to follow:** a similar problem (not the answer to this exercise).

This function cleans up a label and makes it **UPPERCASE**. Two methods, chained from left to right:

```python
def make_label(text):
    return text.strip().upper()
```

Type this example into `playground.py` in the course folder (open it with `code playground.py`), save it, and try it:

```python
$ python3 -i playground.py
>>> make_label('  rail robot \n')
'RAIL ROBOT'
>>> exit()
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, in the file list on the left, click `exercises` → `week1` → `w1d5_strings.py`. (Or press **Ctrl + P**, type `w1d5_strings.py` and press Enter.) The file opens in the editor. Scroll down to the function for this exercise. If the file is already open, click its tab.
2. Replace `pass`. You need two methods from section 3, chained together.
3. Save and try it with `python3 -i`.
4. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k clean_command
   ```
   ✔ You should see `3 passed, 16 deselected`.
5. Check the box for `clean_command`.

> `deselected` means: the tests of the **other** exercises in this file were not run. That is what `-k` does, and it is fine.

### Exercise 2 of 4: `make_topic_name(robot_name, sensor)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson and follow it while you do this exercise, especially [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** build a ROS topic name: lowercase everything, replace spaces with `_`, and join as `/<robot>/<sensor>`.

```python
>>> make_topic_name("Rail Robot 1", "LiDAR")
'/rail_robot_1/lidar'
```

**Example to follow:** a similar problem (not the answer to this exercise).

This function builds a log file name: lowercase, spaces become `-`, then the parts are joined with `_` and `.csv` is added at the end.

```python
def make_file_name(robot_name, date):
    robot = robot_name.lower().replace(" ", "-")
    return robot + "_" + date + ".csv"
```

Type this example into `playground.py` in the course folder (open it with `code playground.py`), save it, and try it:

```python
$ python3 -i playground.py
>>> make_file_name('Rail Robot 1', '2026-10-19')
'rail-robot-1_2026-10-19.csv'
>>> exit()
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, in the file list on the left, click `exercises` → `week1` → `w1d5_strings.py`. (Or press **Ctrl + P**, type `w1d5_strings.py` and press Enter.) The file opens in the editor. Scroll down to the function for this exercise. If the file is already open, click its tab.
2. Replace `pass`. Clean each part with `.lower()` and `.replace(" ", "_")`, then join them with `"/"` (section 3, "Joining strings").
3. Save and try it with `python3 -i`.
4. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k make_topic_name
   ```
   ✔ You should see `3 passed, 16 deselected`.
5. Check the box for `make_topic_name`.

### Exercise 3 of 4: `is_valid_robot_id(robot_id)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson and follow it while you do this exercise, especially [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** return `True` if the text looks like `RR-0042`: exactly 7 characters, 2 uppercase letters, then `-`, then 4 digits. Otherwise return `False`.

```python
>>> is_valid_robot_id("RR-0042")
True
>>> is_valid_robot_id("rr-0042")
False
>>> is_valid_robot_id("RR0042")
False
```

**Example to follow:** a similar problem (not the answer to this exercise).

This function checks if a text looks like a time `HH:MM`, for example `09:30`. It checks the length first, then each part with slicing.

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

Type this example into `playground.py` in the course folder (open it with `code playground.py`), save it, and try it:

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

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, in the file list on the left, click `exercises` → `week1` → `w1d5_strings.py`. (Or press **Ctrl + P**, type `w1d5_strings.py` and press Enter.) The file opens in the editor. Scroll down to the function for this exercise. If the file is already open, click its tab.
2. Replace `pass`. Check the parts **in this order**:
   1. Is `len(robot_id)` exactly 7? If not, `return False` immediately. Otherwise `robot_id[2]` could crash on a short text.
   2. Are the first 2 characters (`robot_id[0:2]`) letters **and** uppercase?
   3. Is character 2 (`robot_id[2]`) a `"-"`?
   4. Are the last 4 characters (`robot_id[3:]`) digits?
3. Save and try it with `python3 -i`. Also try `""` (empty text). It must return `False`, not crash.
4. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k is_valid_robot_id
   ```
   ✔ You should see `9 passed, 10 deselected`.
5. Check the box for `is_valid_robot_id`.

### Exercise 4 of 4: `count_char(text, ch)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson and follow it while you do this exercise, especially [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** count how many times the character `ch` appears in `text`. Use a `for` loop, not `.count()`.

```python
>>> count_char("rail robot", "o")
2
```

**Example to follow:** a similar problem (not the answer to this exercise).

This function counts the spaces in a text with a `for` loop over its characters:

```python
def count_spaces(text):
    count = 0
    for ch in text:
        if ch == " ":
            count = count + 1
    return count
```

Type this example into `playground.py` in the course folder (open it with `code playground.py`), save it, and try it:

```python
$ python3 -i playground.py
>>> count_spaces('rail robot one')
2
>>> count_spaces('ROS')
0
>>> exit()
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, in the file list on the left, click `exercises` → `week1` → `w1d5_strings.py`. (Or press **Ctrl + P**, type `w1d5_strings.py` and press Enter.) The file opens in the editor. Scroll down to the function for this exercise. If the file is already open, click its tab.
2. Replace `pass`. Loop over the text (section 5) and count with the accumulator pattern.
3. Save and try it with `python3 -i`.
4. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d5.py -k count_char
   ```
   ✔ You should see `4 passed, 15 deselected`.
5. Check the box for `count_char`.

### Finally: all of today's tests, and the whole week

```bash
pytest exercises/week1/tests/test_w1d5.py
```

✔ You should see **`19 passed`**. Check the "Tests pass" box.

```bash
pytest exercises/week1
```

✔ You should see **`64 passed`**: all exercises of Days 1–5. Check "The whole week passes" box. If something from an earlier day fails now, fix it before the checkpoint.

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
