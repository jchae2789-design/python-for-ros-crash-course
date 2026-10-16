# How exercises work

Read this guide **before your first exercise** (Week 1, Day 1). Read Part 4 again before Day 3, when the exercises change to functions.

This guide shows the whole process step by step, with real examples of what you will see on your screen.
See [Where to type things](01-how-to-study.md#where-to-type-things) before typing commands.

---

## Part 1: What is an exercise?

Every exercise has **two files**:

| File | Example | What it is | Do you edit it? |
|---|---|---|---|
| **Exercise file** | [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py) | Instructions at the top, and a `TODO` where your code goes | ✅ **Yes**, this is your work |
| **Test file** | [`exercises/week1/tests/test_w1d3.py`](../exercises/week1/tests/test_w1d3.py) | A program that checks your exercise file automatically | ❌ **Never** |

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
In the file list on the left, click [`exercises`](../exercises/) → [`week1`](../exercises/week1/) → the file (for example [`w1d1_hello.py`](../exercises/week1/w1d1_hello.py)). Or press **Ctrl + P**, type the file name and press Enter. You cannot write your code until the file is open in the editor.

**Step 2: Read all the instructions at the top of the file.**
The lines starting with `#` (or the text inside `"""` in a function) tell you:
- what the program must do,
- the **exact** text to print or return,
- at least one **example**,
- **hints** about what to use.

Read the file's instructions twice. Most mistakes come from reading too fast.

**Step 3: Write your code at `TODO` in the file.**
- In **script** exercises (Days 1–2): write below `# TODO: write your code below this line`.
- In **function** exercises (Days 3–5): replace `pass` with your code. Keep the `def ...` line **exactly** as it is.

**Step 4: Save with Ctrl + S.** A white dot ● on the file's tab means it is **not saved**. Tests always check the **saved** file.

**Step 5: Run the saved file.** Use the command in the lesson's numbered steps.
For scripts, run the `python3` command. Enter the example input at the program's prompts.
For functions, run the `python3 -i` command. Type the function calls at `>>>`.

Compare the results with the lesson. Type `exit()` at `>>>` before typing terminal commands.
Parts 3 and 4 show examples.

**Step 6: Run the exercise tests.** Type the lesson's `pytest` command.
For example, this command tests both Day 1 exercises in [`exercises/week1/tests/test_w1d1.py`](../exercises/week1/tests/test_w1d1.py).
After solving both exercises, expect `2 passed`:

```bash
pytest exercises/week1/tests/test_w1d1.py
```

**Step 7: If a test fails, read the terminal error message.**
Correct the named exercise file in VS Code. Return to Step 4.
Part 5 explains the messages. Repeat until all tests pass.

**Step 8: Save your work to GitHub.** Type these commands in order.
After `git push`, open your fork's **Code** tab in your browser. Your saved changes should appear:

```bash
git add .
git commit -m "Week 1 Day 1: hello exercise"
git push
```

---

## Part 3: Worked example: a script exercise (Days 1–2)

This is a **practice example**. Read the code and output below in VS Code or your browser. The `w1d0` files are illustrations. Do not create those files or type their commands.

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

This illustrates running `w1d0_ready.py` in the terminal. Do not type the command; this file does not exist.
The user types `RR-01` at `Robot name:`. The program prints `RR-01 is ready`:

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

This is a read-only illustration. Do not create `w1d0_speed.py` or type its test commands.

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

> **If the terminal shows `None`, inspect the named function in VS Code. Check for missing `return` or incorrect `print`.**

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
- `...F.`: one character per test. [`.`](./) = passed, `F` = failed. 4 of the 5 tests pass.
- `test_speed_status[2.0-MOVING]`: the failing test used `speed = 2.0` and expected `"MOVING"`.
- `assert 'TOO FAST' == 'MOVING'`: **your** function returned `'TOO FAST'` (left), the correct answer is `'MOVING'` (right).

In the read-only `speed_status` example above, read the rule again: *"**more than** 2.0 → TOO FAST"*. Exactly 2.0 is **not** more than 2.0. The bug is `>=`, which should be `>`.

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

Load [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py) with the command below.
At `>>>`, type the calls below, then `exit()`.
After solving `battery_status`, expect the results shown without `>>>`:

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

After changing the file, save with **Ctrl + S**. If Python is still open, type `exit()` at `>>>`. Then type `python3 -i exercises/week1/w1d3_conditions.py` in the terminal to load the saved changes.

### Rules for function exercises

- **Do not rename** the function or its parameters. The test calls it by that exact name. If you rename it, you get `ImportError: cannot import name 'battery_status'`.
- **Use `return`, not `print`**, for the answer.
- **Do not leave `input()` or test lines at the bottom** of a function file. The test loads your file, and an `input()` there gives this error:
  ```
  OSError: pytest: reading from stdin while output is captured!
  ```
  Use the load command and function calls in [Trying a function yourself](#trying-a-function-yourself-step-5) above.

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
| `assert None == ...` | No `return`, or `print` instead of `return` | In VS Code, add `return` inside the function named in the terminal error message |
| `Your program printed: ''` | Script prints nothing | Did you save? Is your code below `TODO`? |
| You run your script and **nothing appears at all** | The file has no code yet (only comments), or your code is not saved | Open the named exercise file in VS Code. Write code below `TODO`. Press **Ctrl + S**; the **●** on the tab disappears |
| `Your script crashed` | Your script has an error | Read the **last line** of the error message in the terminal |
| `Your script did not finish within 10 seconds` | A loop that never ends, or an extra `input()` | In VS Code, open the named exercise file. Check its `while` condition and count its `input()` calls |
| `ImportError: cannot import name ...` | You renamed or deleted the function | In VS Code, restore the original function name in the exercise file named in the terminal error message |
| `SyntaxError` / `IndentationError` | Missing `:` `)` `"` or wrong spaces | In VS Code, open the exercise file named in the terminal error message and go to the line number shown |
| `OSError: pytest: reading from stdin...` | `input()` left in a function file | Remove the extra `input()` from the named exercise file. Save with **Ctrl + S**. Follow the lesson's `python3 -i` steps |
| `asked for more input than expected` | (checkpoint) your loop does not stop | In VS Code, inspect `break` in `main()` in the checkpoint file named in the terminal error message |

### Useful options

These commands run [`Day 3 tests`](../exercises/week1/tests/test_w1d3.py) or all [`Week 1 exercises`](../exercises/week1/).
The comments describe which results each command shows:

```bash
pytest exercises/week1/tests/test_w1d3.py -x          # stop at the first failure (less to read)
pytest exercises/week1/tests/test_w1d3.py -k status   # only tests with "status" in the name
pytest exercises/week1/tests/test_w1d3.py --tb=line   # one line per failure
pytest exercises/week1                                # all exercises of the week
```

Start with `pytest exercises/week1/tests/test_w1d3.py -x` to see the first failing Day 3 test.
Correct the named exercise function in VS Code. Save with **Ctrl + S**.
Repeat the test command until the tests pass.

---

## Part 6: Checkpoints (end of each week)

Checkpoints are bigger programs with menus and loops. The test **plays the user**: it types a fixed list of answers, one for each `input()` your program asks, and checks what your program prints.

For example, the Week 1 game test types `50`, `abc`, `25`, `42` and expects to see `Too high`, `Please enter a number.`, `Too low`, `Correct!` and `You got it in 3 tries!`.

This means:
- Print messages **exactly** as written in the [checkpoint README](../checkpoints/week1/README.md).
- Ask for input **in the same order** as described.
- If your loop asks for more input than the test has, you get: `Your program asked for more input than expected (is your loop stopping?)`.

Save the checkpoint files in VS Code. Run [`checkpoints/week1/converter.py`](../checkpoints/week1/converter.py) with `python3 checkpoints/week1/converter.py`.
Enter the example inputs from [`checkpoints/week1/README.md`](../checkpoints/week1/README.md). End with `q` at `Choose:` to return to the terminal.

Then run [`checkpoints/week1/guess.py`](../checkpoints/week1/guess.py) with `python3 checkpoints/week1/guess.py`.
Play the game and compare its output with the checkpoint README.
The secret is random, so your guesses can differ. Show both programs to your mentor.

---

## Part 7: The rules

1. **Never edit files in [`tests/`](../exercises/week1/tests/) folders.** Your mentor sees every change on GitHub.
2. **Do not rename** exercise files or functions.
3. **Fix one failure at a time**, starting from the top.
4. **Stuck for 20 minutes?** Write down the exact error message and what you tried, and ask your mentor.
5. **Push at the end of every day**, even if not all tests pass. On GitHub, your commit shows ❌ until everything passes. That is fine during the week. By Friday it should be ✅.
