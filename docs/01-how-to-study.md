# How to study in this course

> ### Where to type things
>
> Unless a step says otherwise, type commands in the **terminal**.
> Use the course folder `~/code/python-for-ros-crash-course`.
> Keep the venv active: the prompt starts with `(.venv)`.
>
> Type text after `>>>` at Python's **`>>>` prompt**.
> Do not type the `$` or `>>>` prompt symbols.
> Type `exit()` at `>>>` before returning to terminal commands.
>
> Edit files in **VS Code**.

## The daily loop

Your checklist in [`progress/`](../progress/) (for example [progress/week1.md](../progress/week1.md)) lists every step in order.
Open the checklist in VS Code. Follow the steps from top to bottom.
Change completed boxes from `[ ]` to `[x]`. Save with **Ctrl + S**.

The steps of a normal day are:

1. **Start the day:** open the terminal with **Ctrl + Alt + T**.
   Type these commands in order:
   ```bash
   cd ~/code/python-for-ros-crash-course
   source .venv/bin/activate
   code .
   ```
2. **Read the lesson** for today in [`lessons/week1/`](../lessons/week1/).
   Type each example yourself. Follow the lesson's instructions for the editor or `>>>` prompt.

   For file examples, open `playground.py` with `code playground.py`.
   Type the example in VS Code. Save with **Ctrl + S**.

   Run `python3 playground.py`. Compare the output with the lesson's results.

   Then change a value in `playground.py`. Save with **Ctrl + S**.
   Run `python3 playground.py` again to see the difference.
3. **Do the "Try it" tasks** in the lesson. They are not tested, but they prepare you for the exercises.
4. **Solve the exercises.** Open the exercise file named in today's lesson.
   Read the instructions at the top. Write code at `TODO`. Save with **Ctrl + S**.
5. **Run the tests.** Type the `pytest` command from the exercise steps.
   Compare the result with the lesson's expected count.
6. **Check in** with your mentor.
7. **Write your log, check off your progress list, commit and push.**

---

## Running tests

The tests check your code automatically. For the full step-by-step process with examples, open [How exercises work](02-how-exercises-work.md) in VS Code. Type this command to run [`test_w1d3.py`](../exercises/week1/tests/test_w1d3.py):

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

In VS Code, inspect `battery_status` in [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py): follow the conditions with `percent` set to `89`. The function should return `"OK"`.

### Useful pytest options

These commands run [`Day 3 tests`](../exercises/week1/tests/test_w1d3.py) or all [`Week 1 exercises`](../exercises/week1/).
The comments describe which results each command shows:

```bash
pytest exercises/week1/tests/test_w1d3.py -x          # stop at the first failure
pytest exercises/week1/tests/test_w1d3.py -k status   # only tests with "status" in the name
pytest exercises/week1 --tb=line                      # short error messages
```

---

## Running your code yourself

Tests tell you **if** your code is right. To investigate a failure, call the function yourself.

Load [`exercises/week1/w1d3_conditions.py`](../exercises/week1/w1d3_conditions.py) with the command below.
At `>>>`, type `battery_status(89)`. After solving the exercise, expect `'OK'`.
Type `exit()` at `>>>` to return to the terminal:

```bash
python3 -i exercises/week1/w1d3_conditions.py
```

```python
>>> battery_status(89)      # what do I get?
```

In VS Code, add `print(...)` inside `battery_status` to display variable values. Save with **Ctrl + S**.
At `>>>`, type `exit()` if Python is still open.
Then repeat the load command above and call `battery_status(89)` at `>>>`.

After debugging, remove the extra `print(...)` lines. Save the file.

---

## Saving your work with Git

At the end of every day (or more often), type these commands in order:

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
The new log uses today's date: `logs/YYYY-MM-DD.md`.

```bash
cp logs/TEMPLATE.md logs/$(date +%F).md
```

Then open that dated file in VS Code. Replace the placeholders with your answers.
Save with **Ctrl + S**.

Write honestly. "I did not understand `elif`" is a great log entry, because now your mentor can help you. The log is also part of your official training record.

---

## When you are stuck

1. **Read the error message in the terminal**, especially the **last line**. It usually says exactly what is wrong.
2. Add `print(...)` calls for the variables in your exercise file. Save with **Ctrl + S**.
   Rerun the exercise using the lesson steps. The terminal shows the variable values.
3. **Re-read** the part of the lesson about this topic.
4. Still stuck after **20 minutes**? Write the question in your log and ask your mentor. Show:
   - what you tried,
   - the exact error message,
   - what you expected to happen.

---

## Getting new lessons

Your mentor adds new weeks to the main course. To get them into your fork:

1. On GitHub, open your fork and click **Sync fork** → **Update branch**.
2. Type the commands below in order. They download the new lessons and install packages from [`requirements.txt`](../requirements.txt).
   The new week's files should appear in VS Code:
   ```bash
   git pull
   pip install -r requirements.txt
   ```
