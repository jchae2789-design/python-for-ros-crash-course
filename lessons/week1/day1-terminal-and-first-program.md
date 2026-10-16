# Week 1 · Day 1: The terminal and your first program

**You will learn:** how to move around in the terminal, how to run Python, how to print text, and how to read an error message.

**Why this matters for robots:** with ROS 2 you start robots, watch sensor data and fix problems almost only from the terminal. A robot engineer who is comfortable in the terminal is much faster.

---

## 1. The terminal

Open a terminal (**Ctrl + Alt + T**). The text before the cursor is the **prompt**. It shows your user name and the folder you are in, for example:

```
minjun@robot-pc:~$
```

`~` means your **home folder** (`/home/minjun`).

### Moving around

| Command | What it does | Example |
|---|---|---|
| `pwd` | **p**rint **w**orking **d**irectory: where am I? | `pwd` |
| `ls` | **l**i**s**t the files in this folder | `ls` |
| `cd folder` | **c**hange **d**irectory: go into a folder | `cd code` |
| `cd ..` | go up one folder | `cd ..` |
| `cd ~` | go back to your home folder | `cd ~` |
| `mkdir name` | **m**a**k**e a new **dir**ectory (folder) | `mkdir test` |
| `cat file` | show what is inside a file | `cat README.md` |
| `clear` | clean the screen | `clear` |

### Try it

Type each line and look at the result:

```bash
cd ~
pwd
ls
mkdir playground
cd playground
pwd
cd ..
ls
```

You should see your new `playground` folder in the last `ls`.

### Three shortcuts that save hours

- **Tab**: completes names for you. Type `cd pla` and press Tab. It becomes `cd playground/`.
- **↑ (up arrow)**: shows your last command again. Press it more to go further back.
- **Ctrl + C**: stops a program that is running (for example, one that never ends).

In ROS you type long names like `/rail_robot/lidar/scan`. Use Tab all the time!

---

## 2. Talking to Python

Python has an **interactive mode**: you type one line, Python answers immediately.

```bash
python3
```

You see `>>>`. Python is waiting for you. Try:

```python
>>> 2 + 3
5
>>> 10 * 7
70
>>> "robot"
'robot'
```

Leave interactive mode with:

```python
>>> exit()
```

Use interactive mode to test small ideas quickly. For real programs, we write **files**.

---

## 3. Your first program file

A Python program is a text file that ends in `.py`. Python reads it **from top to bottom** and runs each line.

Go to the course folder and create a test file:

```bash
cd ~/code/python-for-ros-crash-course
code playground.py
```

Write this in VS Code and save (**Ctrl + S**):

```python
print("Hello!")
print("I am a robot.")
```

Run it in the terminal:

```bash
python3 playground.py
```

Output:

```
Hello!
I am a robot.
```

### `print()`

`print()` shows something on the screen. Text must be inside quotes. Both `"double"` and `'single'` quotes work:

```python
print("Battery OK")
print('Battery OK')       # same result
print()                   # prints an empty line
print("Speed:", 2.5)      # a comma puts a space between the parts
print(3 + 4)              # Python calculates first, then prints 7
```

### Comments

Everything after `#` is a **comment**. Python ignores it. Comments are notes for humans:

```python
# This program checks the robot battery
print("Battery OK")  # comments can also go at the end of a line
```

### Try it

In `playground.py`, write a program that prints:

```
=== Robot RR-01 ===
Speed: 0.5 m/s

Ready to start.
```

(There is an empty line before `Ready to start.`)

---

## 4. Errors are your friends

Everyone makes errors, also professional engineers, every day. The important skill is **reading** them.

Change your file to this (the closing quote is missing):

```python
print("Hello!)
```

Run it:

```
  File "/home/minjun/code/python-for-ros-crash-course/playground.py", line 1
    print("Hello!)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

How to read it:

1. **Last line first:** `SyntaxError: unterminated string literal`. A text (string) is not closed.
2. **Line number:** `line 1`. The error is on line 1.
3. **The `^`** points to where the problem starts.

Another common one. Change the file to:

```python
prnt("Hello!")
```

```
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```

Python does not know `prnt`. It even tells you what you probably meant!

### Common errors on Day 1

| Error | Usual cause |
|---|---|
| `SyntaxError` | missing quote `"` or bracket `)` |
| `NameError` | typo in a name, or text without quotes: `print(Hello)` |
| `IndentationError` | spaces at the start of a line where there should be none |
| `python3: can't open file` | you are in the wrong folder, or the file name has a typo. Use `ls` and `pwd`! |

---

## 5. Exercises

> First time? Read [How exercises work](../../docs/02-how-exercises-work.md), Parts 1–3, before you start.

Delete `playground.py` when you are done playing (`rm playground.py`).

Open the exercise files in VS Code:

1. `exercises/week1/w1d1_hello.py`
2. `exercises/week1/w1d1_robot_card.py`

Read the instructions at the top of each file, write your code under `TODO`, and run it:

```bash
python3 exercises/week1/w1d1_hello.py
```

When it looks right, run the tests:

```bash
pytest exercises/week1/tests/test_w1d1.py
```

The tests check the output **exactly**: every capital letter, space and punctuation mark counts. `Hello, ROS!` is not the same as `Hello ROS!` or `hello, ros!`.

---

## 6. Before you finish today

- [ ] `pytest exercises/week1/tests/test_w1d1.py` shows **2 passed**
- [ ] I can use `pwd`, `ls`, `cd`, `mkdir` without looking
- [ ] I wrote my daily log in `logs/`
- [ ] I committed and pushed:
  ```bash
  git add .
  git commit -m "Week 1 Day 1: first programs"
  git push
  ```

**Next:** [Day 2: Variables, numbers and input](day2-variables-numbers-input.md)
