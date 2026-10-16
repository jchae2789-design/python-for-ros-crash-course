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

You can keep `playground.py`. You will use it for the examples below. Git ignores it, so it is never committed.

**How to do the exercises:** do them **in order**, one at a time. Each exercise below has numbered steps. Follow them from 1 to the end, then go to the next exercise. If a step does not work, look at [How exercises work, Part 5](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

Today's exercises check your output **exactly**: every capital letter, space and punctuation mark counts. `Hello, ROS!` is not the same as `Hello ROS!` or `hello, ros!`.

### Exercise 1 of 2: Hello, ROS!

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson and follow it while you do this exercise, especially [Part 3: a script exercise](../../docs/02-how-exercises-work.md#part-3-worked-example-a-script-exercise-days-12) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** write a program that prints one line: `Hello, ROS!`

**What it should look like:**

```
$ python3 exercises/week1/w1d1_hello.py
Hello, ROS!
```

**Example to follow:** a similar problem (not the answer to this exercise).

This program greets the robot team:

```python
print("Good morning, robot team!")
```

Type this example into `playground.py` in the course folder (open it with `code playground.py`), save it, and run it:

```
$ python3 playground.py
Good morning, robot team!
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, in the file list on the left, click `exercises` → `week1` → `w1d1_hello.py`. (Or press **Ctrl + P**, type `w1d1_hello.py` and press Enter.) The file opens in the editor.
2. Read the instructions at the top of the file.
3. Write your code on the empty line below `# TODO: write your code below this line`. You need one `print()`.
4. Save the file: **Ctrl + S**. The **●** on the file's tab disappears when it is saved.
5. Run it in the terminal:
   ```bash
   python3 exercises/week1/w1d1_hello.py
   ```
   ✔ You should see `Hello, ROS!`
   ✘ If **nothing appears at all**, your file has no code yet or is not saved. Go back to step 3.
6. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d1.py -k hello
   ```
   ✔ You should see `1 passed, 1 deselected`. If not, read the message, fix your code and go back to step 4.
7. Check the box for this exercise in [progress/week1.md](../../progress/week1.md).

> `deselected` means: the tests of the **other** exercises in this file were not run. That is what `-k` does, and it is fine.

### Exercise 2 of 2: Robot info card

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson and follow it while you do this exercise, especially [Part 3: a script exercise](../../docs/02-how-exercises-work.md#part-3-worked-example-a-script-exercise-days-12) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** write a program that prints exactly these 3 lines:

```
Robot: RR-01
Type: Rail robot
Status: READY
```

**Example to follow:** a similar problem (not the answer to this exercise).

This program prints a card for a drone, using one `print()` per line:

```python
print("Drone: DR-07")
print("Type: Quadcopter")
print("Status: CHARGING")
```

Type this example into `playground.py` in the course folder (open it with `code playground.py`), save it, and run it:

```
$ python3 playground.py
Drone: DR-07
Type: Quadcopter
Status: CHARGING
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, in the file list on the left, click `exercises` → `week1` → `w1d1_robot_card.py`. (Or press **Ctrl + P**, type `w1d1_robot_card.py` and press Enter.) The file opens in the editor.
2. Read the instructions at the top of the file.
3. Write your code below `TODO`. Use one `print()` for each line.
4. Save: **Ctrl + S**. The **●** on the file's tab disappears when it is saved.
5. Run it:
   ```bash
   python3 exercises/week1/w1d1_robot_card.py
   ```
   ✔ You should see the 3 lines above. Compare them letter by letter.
   ✘ If **nothing appears at all**, your file has no code yet or is not saved. Go back to step 3.
6. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d1.py -k robot_card
   ```
   ✔ You should see `1 passed, 1 deselected`.
7. Check the box for this exercise in your checklist.

### Finally: all of today's tests

```bash
pytest exercises/week1/tests/test_w1d1.py
```

✔ You should see **`2 passed`**. Check the "Tests pass" box in your checklist.

---

## 6. Before you finish today

Check off **Day 1** in your checklist: [progress/week1.md](../../progress/week1.md). Only start Day 2 when every Day 1 box is checked.

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
