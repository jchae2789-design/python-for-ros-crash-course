# How exercises work

Read this guide **before your first exercise** (Week 1, Day 1). Read Part 4 again before Day 3, when the exercises change to functions.

This guide shows the whole process step by step, with real examples of what you will see on your screen.

---

## Part 1: What is an exercise?

Every exercise has **two files**:

| File | Example | What it is | Do you edit it? |
|---|---|---|---|
| **Exercise file** | `exercises/week1/w1d3_conditions.py` | Instructions at the top, and a `TODO` where your code goes | ✅ **Yes**, this is your work |
| **Test file** | `exercises/week1/tests/test_w1d3.py` | A program that checks your exercise file automatically | ❌ **Never** |

The file names tell you where the exercise belongs:

```
w1d3_conditions.py
│ │  └── topic
│ └──── day 3
└────── week 1
```

The test file for `w1d3_...` is always `tests/test_w1d3.py`.

### What the tests do

A test is a robot that checks your work. It:

1. runs your code with **many different inputs**,
2. compares the result with the **correct answer**,
3. tells you **passed** ✅ or **failed** ❌, and when it fails, it says **what was wrong**.

You are finished with an exercise when **all of its tests pass**.

---

## Part 2: The 8 steps, every time

Do these steps for **every** exercise, in this order.

**Step 1: Open the exercise file in VS Code.**
In the file list on the left, click `exercises` → `week1` → the file (for example `w1d1_hello.py`). Or press **Ctrl + P**, type the file name and press Enter. You cannot write your code until the file is open in the editor.

**Step 2: Read all the instructions at the top.**
The lines starting with `#` (or the text inside `"""` in a function) tell you:
- what the program must do,
- the **exact** text to print or return,
- at least one **example**,
- **hints** about what to use.

Read them twice. Most mistakes come from reading too fast.

**Step 3: Write your code at `TODO`.**
- In **script** exercises (Days 1–2): write below `# TODO: write your code below this line`.
- In **function** exercises (Days 3–5): replace `pass` with your code. Keep the `def ...` line **exactly** as it is.

**Step 4: Save the file.** Press **Ctrl + S**. A white dot ● on the file's tab means it is **not saved**. Tests always check the **saved** file.

**Step 5: Try your code yourself.** See Part 3 (scripts) or Part 4 (functions) for how.

**Step 6: Run the tests.** In the terminal, from the course folder, with the venv active:

```bash
pytest exercises/week1/tests/test_w1d1.py
```

**Step 7: If a test fails, read the message, fix your code, and go back to Step 4.** Part 5 explains how to read the messages. Repeat until everything passes. This is normal! Professionals do this loop all day.

**Step 8: Save your work to GitHub.**

```bash
git add .
git commit -m "Week 1 Day 1: hello exercise"
git push
```

---

## Part 3: Worked example: a script exercise (Days 1–2)

This is a **practice example**. It is not in your exercises folder, so just read along.

### The exercise file: `w1d0_ready.py`

```python
# Ask for the robot name:   Robot name:
# Then print:               <name> is ready
#
# Example: if the user types RR-01, print "RR-01 is ready".

# TODO: write your code below this line
```

### Running the tests before writing any code

```bash
pytest exercises/week1/tests/test_w1d0.py
```

```
E       AssertionError: Your program printed: ''
E       assert 'RR-01 is ready' in ''
```

How to read this:
- `Your program printed: ''`: `''` is **empty text**. Your program printed nothing, which is correct, because there is no code yet.
- `assert 'RR-01 is ready' in ''`: the test looked for `RR-01 is ready` in your output and did not find it.

### Attempt 1: a crash

```python
name = input("Robot name: ")
print(name + " is ready" + 1)
```

```
Your script crashed. Error message:
Traceback (most recent call last):
  File ".../exercises/week1/w1d0_ready.py", line 2, in <module>
    print(name + " is ready" + 1)
          ~~~~~~~~~~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

How to read this:
- `Your script crashed`: the program stopped with an error before it finished.
- `line 2`: the problem is on line 2.
- The **last line** says what is wrong: you cannot add a number (`1`) to a text.

### Attempt 2: correct

```python
name = input("Robot name: ")
print(name + " is ready")
```

```
1 passed in 0.12s
```

Done. ✅

### Trying a script yourself (Step 5)

Run it like any program and type the example input:

```bash
python3 exercises/week1/w1d0_ready.py
```

```
Robot name: RR-01
RR-01 is ready
```

### How the test "types" for you

For script exercises, the test runs your program and types the input automatically. For example, it types `RR-01` and presses Enter. Then it reads what your program printed.

So **do not cheat by printing a fixed answer** like `print("RR-01 is ready")`. The real tests try **several different inputs**, for example `5000`/`2000`, then `3300`/`1100`, then `1000`/`3000`. A fixed answer fails them.

---

## Part 4: Worked example: a function exercise (Days 3–5)

From Day 3 on, exercises are **functions**. The test does not run your file as a program. Instead it **calls your function** with different values and checks what it **returns**.

### The exercise file: `w1d0_speed.py`

```python
def speed_status(speed):
    """Return a status word for a robot speed (m/s).

    - exactly 0          -> "STOPPED"
    - more than 2.0      -> "TOO FAST"
    - anything else      -> "MOVING"

    Example: speed_status(1.0) returns "MOVING"
    """
    # TODO
    pass
```

### Running the tests before writing any code

```
E       AssertionError: assert None == 'STOPPED'
E        +  where None = speed_status(0)
...
4 failed in 0.15s
```

How to read this:
- `speed_status(0)`: the test called your function with `speed = 0`.
- `assert None == 'STOPPED'`: it expected `'STOPPED'` but got `None`.
- `None` means "nothing". Your function did not **return** anything. With only `pass`, that is expected.

> 💡 **If you ever see `None` in a failing test, check for a missing `return`, or a `print` where you need `return`.**

### Attempt 1: almost correct

```python
def speed_status(speed):
    if speed == 0:
        return "STOPPED"
    elif speed >= 2.0:
        return "TOO FAST"
    else:
        return "MOVING"
```

```
...F.
FAILED exercises/week1/tests/test_w1d0.py::test_speed_status[2.0-MOVING]
E       AssertionError: assert 'TOO FAST' == 'MOVING'
1 failed, 4 passed in 0.14s
```

How to read this:
- `...F.`: one character per test. `.` = passed, `F` = failed. 4 of the 5 tests pass.
- `test_speed_status[2.0-MOVING]`: the failing test used `speed = 2.0` and expected `"MOVING"`.
- `assert 'TOO FAST' == 'MOVING'`: **your** function returned `'TOO FAST'` (left), the correct answer is `'MOVING'` (right).

Now go back to the instructions: *"**more than** 2.0 → TOO FAST"*. Exactly 2.0 is **not** more than 2.0. The bug is `>=`, which should be `>`.

> 💡 **Tests love edge values** like exactly `2.0`, `0`, `90`, `15`. When only one test fails, it is usually `>` vs `>=` or `<` vs `<=`.

### Attempt 2: correct

```python
    elif speed > 2.0:
```

```
5 passed in 0.12s
```

Done. ✅

### Trying a function yourself (Step 5)

Use Python's interactive mode with `-i`. It loads your file and then lets you call your functions:

```bash
python3 -i exercises/week1/w1d3_conditions.py
```

```python
>>> battery_status(55)
'OK'
>>> battery_status(90)
'FULL'
>>> exit()
```

After changing your file, **exit and start `python3 -i` again**. It does not reload by itself.

### Rules for function exercises

- **Do not rename** the function or its parameters. The test calls it by that exact name. If you rename it, you get `ImportError: cannot import name 'battery_status'`.
- **Use `return`, not `print`**, for the answer.
- **Do not leave `input()` or test lines at the bottom** of a function file. The test loads your file, and an `input()` there gives this error:
  ```
  OSError: pytest: reading from stdin while output is captured!
  ```
  Use `python3 -i` (above) to try your function instead.

---

## Part 5: Reading test results

### The summary line (always at the bottom)

| You see | Meaning |
|---|---|
| `5 passed` | All done ✅ |
| `1 failed, 4 passed` | Almost there. Fix the one that failed |
| `5 failed` | Nothing works yet. Normal before you start. Otherwise, look for a crash or a missing `return` |
| `1 error` | The test could not even **load** your file. Look for `SyntaxError`, `IndentationError`, `ImportError` or `OSError ... reading from stdin` |

### The name of a failing test

```
FAILED exercises/week1/tests/test_w1d3.py::test_battery_status[89-OK]
                     └── test file           └── what is tested  └── the input and expected answer
```

`[89-OK]` means: the test used `89` and expected `OK`.

### The `E` lines

The lines starting with `E` are the **error**. The most important is usually:

```
E       assert 'FULL' == 'OK'
               └ yours   └ correct
```

**Left = what your code gave. Right = what was expected.**

### Common messages and what to do

| Message | Cause | Fix |
|---|---|---|
| `assert None == ...` | No `return`, or `print` instead of `return` | Add `return` |
| `Your program printed: ''` | Script prints nothing | Did you save? Is your code below `TODO`? |
| You run your script and **nothing appears at all** | The file has no code yet (only comments), or your code is not saved | Open the file, write code below `TODO`, press **Ctrl + S** and check that the **●** on the tab is gone |
| `Your script crashed` | Your script has an error | Read the **last line** of the error message |
| `Your script did not finish within 10 seconds` | A loop that never ends, or an extra `input()` | Check that your `while` condition becomes `False`, and count your `input()` calls |
| `ImportError: cannot import name ...` | You renamed or deleted the function | Use the exact name from the starter file |
| `SyntaxError` / `IndentationError` | Missing `:` `)` `"` or wrong spaces | Go to the line number shown |
| `OSError: pytest: reading from stdin...` | `input()` left in a function file | Remove it and use `python3 -i` to try your function |
| `asked for more input than expected` | (checkpoint) your loop does not stop | Check your `break` |

### Useful options

```bash
pytest exercises/week1/tests/test_w1d3.py -x          # stop at the first failure (less to read)
pytest exercises/week1/tests/test_w1d3.py -k status   # only tests with "status" in the name
pytest exercises/week1/tests/test_w1d3.py --tb=line   # one line per failure
pytest exercises/week1                                # all exercises of the week
```

Start with `-x`. Fix **one** failure at a time, from top to bottom.

---

## Part 6: Checkpoints (end of each week)

Checkpoints are bigger programs with menus and loops. The test **plays the user**: it types a fixed list of answers, one for each `input()` your program asks, and checks what your program prints.

For example, the Week 1 game test types `50`, `abc`, `25`, `42` and expects to see `Too high`, `Please enter a number.`, `Too low`, `Correct!` and `You got it in 3 tries!`.

This means:
- Print messages **exactly** as written in the checkpoint README.
- Ask for input **in the same order** as described.
- If your loop asks for more input than the test has, you get: `Your program asked for more input than expected (is your loop stopping?)`.

Always also **run the checkpoint yourself** and play it. Your mentor will ask you to demonstrate it.

---

## Part 7: The rules

1. **Never edit files in `tests/` folders.** Your mentor sees every change on GitHub.
2. **Do not rename** exercise files or functions.
3. **Fix one failure at a time**, starting from the top.
4. **Stuck for 20 minutes?** Write down the exact error message and what you tried, and ask your mentor.
5. **Push at the end of every day**, even if not all tests pass. On GitHub, your commit shows ❌ until everything passes. That is fine during the week. By Friday it should be ✅.
