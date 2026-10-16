# How to study in this course

## Where to type things

> Type commands in the **VS Code terminal**, the bottom panel below the editor. Open it with **Ctrl + `** or **Terminal → New Terminal**.
> It already starts in the course folder `~/code/python-for-ros-crash-course`, with the venv on: the prompt shows `(.venv)`.
> If the folder is wrong, type `cd ~/code/python-for-ros-crash-course` in the VS Code terminal.
> If `(.venv)` is missing, close the terminal with its **trash icon** and open a new one. If it is still missing, type `source .venv/bin/activate` in the VS Code terminal.
>
> Type text after `>>>` at Python's **`>>>` prompt** in that same VS Code terminal. These interactive experiments do not edit a file unless the step names one.
> Do not type the `$` or `>>>` prompt symbols.
> Type `exit()` at Python's `>>>` prompt before returning to VS Code terminal commands.
>
> Edit and save files in the **VS Code editor**, above the terminal.

## The daily loop

Your checklist in [`progress/`](../progress/) (for example [progress/week1.md](../progress/week1.md)) lists every step in order.
Open the checklist in the VS Code editor. Follow the steps from top to bottom.
Change completed boxes from `[ ]` to `[x]`. Save with **Ctrl + S**.

The steps of a normal day are:

1. **Start the day:** open VS Code. It reopens the course folder; otherwise choose **File → Open Recent** and select the course folder. Open [`progress/week1.md`](../progress/week1.md) in the VS Code editor. Open the **VS Code terminal** with **Ctrl + `** and check that the prompt shows `(.venv)` (see [Where to type things](#where-to-type-things)).
2. In the VS Code editor, **read today's lesson file** in [`lessons/week1/`](../lessons/week1/).
   Type each example yourself. Follow the lesson's instructions for the editor or `>>>` prompt.

   For file examples, in the VS Code terminal, type `code playground.py` to open `playground.py` in the same window.
   In the VS Code editor, type the example into `playground.py`. Save `playground.py` with **Ctrl + S**.

   In the VS Code terminal, run `python3 playground.py`. Compare the output with the lesson's results.

   In the VS Code editor, change a value in `playground.py`. Save `playground.py` with **Ctrl + S**.
   In the VS Code terminal, run `python3 playground.py` again to see the difference.
3. **Do the "Try it" tasks** in today's lesson file: use the VS Code editor for `playground.py`, the VS Code terminal to run it, or Python's **`>>>` prompt** for interactive experiments, as the task directs. These tasks are not tested, but they prepare you for the exercises.
4. **Solve the exercises.** In the VS Code editor, open the exercise file named in today's lesson (for example [`w1d1_hello.py`](../exercises/week1/w1d1_hello.py)).
   Read the instructions at the top. Write code at `TODO`. Save with **Ctrl + S**.
5. **Run the tests.** In the VS Code terminal, type the `pytest` command from the exercise steps for the file you just edited (for example `w1d1_hello.py`).
   Compare the result with the lesson's expected count.
6. **Check in** with your mentor: show your exercise file (for example `w1d1_hello.py`) in the VS Code editor and its results in the VS Code terminal.
7. In the VS Code editor, **write your dated log** (`logs/YYYY-MM-DD.md`) and **check off [`progress/week1.md`](../progress/week1.md)**. Save both files with **Ctrl + S**. In the VS Code terminal, **commit and push** those files and your exercise files using [Saving your work with Git](#saving-your-work-with-git).

---

## Running tests

The tests check your code automatically. For the full step-by-step process with examples, open [How exercises work](02-how-exercises-work.md) in the VS Code editor. In the VS Code terminal, type this command to run [`test_w1d3.py`](../exercises/week1/tests/test_w1d3.py):

```bash
pytest exercises/week1/tests/test_w1d3.py
```

Possible results:

- `5 passed`: all done. 🎉
- `2 failed, 3 passed`: some parts are still wrong.

### How to read a failing test

When a test fails, pytest shows something like this:

```
FAILED exercises/week1/tests/test_w1d3.py::test_battery_status[89-OK]
    assert battery_status(percent) == expected
E   AssertionError: assert 'FULL' == 'OK'
```

Read it like this:

- `test_battery_status[89-OK]`: the test called `battery_status(89)` and expected `"OK"`.
- `assert 'FULL' == 'OK'`: your function gave back `'FULL'`, but `'OK'` was expected.

In the VS Code editor, inspect `battery_status` in [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py): follow the conditions with `percent` set to `89`. The function should return `"OK"`.

### Useful pytest options

In the VS Code terminal, these commands run [`Day 3 tests`](../exercises/week1/tests/test_w1d3.py) or all [`Week 1 exercises`](../exercises/week1/).
The comments describe which results each command shows:

```bash
pytest exercises/week1/tests/test_w1d3.py -x          # stop at the first failure
pytest exercises/week1/tests/test_w1d3.py -k status   # only tests with "status" in the name
pytest exercises/week1 --tb=line                      # short error messages
```

---

## Running your code yourself

Tests tell you **if** your code is right. To investigate a failure, call the function yourself.

In the VS Code terminal, load [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py) with the command below.
At `>>>`, type `battery_status(89)`. After solving the exercise, expect `'OK'`.
Type `exit()` at `>>>` to return to the VS Code terminal:

```bash
python3 -i exercises/week1/w1d3_conditions.py
```

```python
>>> battery_status(89)      # what do I get?
```

In the VS Code editor, in `w1d3_conditions.py`, add `print(...)` inside `battery_status` to display variable values. Save with **Ctrl + S**.
At `>>>`, type `exit()` if Python is still open.
Then repeat the load command above and call `battery_status(89)` at `>>>`.

After debugging, in the VS Code editor, remove the extra `print(...)` lines from `w1d3_conditions.py`. Save `w1d3_conditions.py` with **Ctrl + S**.

---

## Saving your work with Git

At the end of every day (or more often), save your exercise files, dated log, and [`progress/week1.md`](../progress/week1.md) in the VS Code editor. In the VS Code terminal, type these commands in order:

```bash
git status                                  # what did I change?
git add .                                   # prepare all changes
git commit -m "Week 1 Day 3: conditions"    # save them with a message
git push                                    # send them to GitHub
```

Write commit messages that say **what** you did: `"Week 1 Day 4: finish loops exercises"`, not `"update"`.

On GitHub, your fork shows a ✅ or ❌ next to each commit. ❌ only means that some exercises are not finished yet. That is fine during the week. By Friday, the week should be ✅.

---

## The daily log

Every day, copy [`logs/TEMPLATE.md`](../logs/TEMPLATE.md) with the command below.
In the VS Code terminal, type the copy command. The new log uses today's date: `logs/YYYY-MM-DD.md`.

```bash
cp logs/TEMPLATE.md logs/$(date +%F).md
```

Then open that dated file in the VS Code editor. Replace the placeholders with your answers.
Save with **Ctrl + S**.

Write honestly. "I did not understand `elif`" is a great log entry, because now your mentor can help you. The log is also part of your official training record.

---

## When you are stuck

1. **Read the error message for your exercise file in the VS Code terminal**, especially the **last line**. It usually says exactly what is wrong.
2. In the VS Code editor, add `print(...)` calls for the variables in the exercise file named in the VS Code terminal error message. Save that file with **Ctrl + S**.
   Rerun the exercise using the lesson steps. The terminal shows the variable values.
3. In the VS Code editor, **re-read** the part of today's lesson file about this topic.
4. Still stuck after **20 minutes**? In the VS Code editor, write the question in `logs/YYYY-MM-DD.md`, save it with **Ctrl + S**, and ask your mentor. Show:
   - what you tried,
   - the exact error message,
   - what you expected to happen.

---

## Getting new lessons

Your mentor adds new weeks to the main course. To get them into your fork:

1. On GitHub, open your fork and click **Sync fork** → **Update branch**.
2. In the VS Code terminal, type the commands below in order. They download the new lessons and install packages from [`requirements.txt`](../requirements.txt).
   The new week's files should appear in VS Code:
   ```bash
   git pull
   pip install -r requirements.txt
   ```
