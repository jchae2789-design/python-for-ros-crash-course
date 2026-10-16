# How to study in this course

## The daily loop

Your checklist in `progress/` (for example [progress/week1.md](../progress/week1.md)) lists every step in order. Do them top to bottom and check each box when it is done. The steps of a normal day are:

1. **Start the day:** open the terminal, go to the course and activate the venv.
   ```bash
   cd ~/code/python-for-ros-crash-course
   source .venv/bin/activate
   code .
   ```
2. **Read the lesson** for today. Every time you see a code example, **type it yourself** in the terminal (`python3`) or in a test file and run it. Change it a little and see what happens.
3. **Do the "Try it" tasks** in the lesson. They are not tested, but they prepare you for the exercises.
4. **Solve the exercises.** Open the exercise file, read the instructions at the top, and write your code where it says `TODO`.
5. **Run the tests** until they pass.
6. **Check in** with your mentor.
7. **Write your log, check off your progress list, commit and push.**

---

## Running tests

The tests check your code automatically. For the full step-by-step process with examples, read [How exercises work](02-how-exercises-work.md).

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

So: check what your code does when `percent` is 89.

### Useful pytest options

```bash
pytest exercises/week1/tests/test_w1d3.py -x          # stop at the first failure
pytest exercises/week1/tests/test_w1d3.py -k status   # only tests with "status" in the name
pytest exercises/week1 --tb=line                      # short error messages
```

---

## Running your code yourself

Tests tell you **if** your code is right. To find out **why** it is wrong, run your code yourself and use `print()`.

For exercises with a function, load the file in interactive mode and call the function:

```bash
python3 -i exercises/week1/w1d3_conditions.py
```

```python
>>> battery_status(89)      # what do I get?
```

Inside your function you can also add `print(...)` lines to see the values of variables. Remove them when you are done.

---

## Saving your work with Git

At the end of every day (or more often):

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

Every day, copy the template and fill it in:

```bash
cp logs/TEMPLATE.md logs/$(date +%F).md
```

Write honestly. "I did not understand `elif`" is a great log entry, because now your mentor can help you. The log is also part of your official training record.

---

## When you are stuck

1. **Read the error message**, especially the **last line**. It usually says exactly what is wrong.
2. **Print** your variables to see what they really contain.
3. **Re-read** the part of the lesson about this topic.
4. Still stuck after **20 minutes**? Write the question in your log and ask your mentor. Show:
   - what you tried,
   - the exact error message,
   - what you expected to happen.

---

## Getting new lessons

Your mentor adds new weeks to the main course. To get them into your fork:

1. On GitHub, open your fork and click **Sync fork** → **Update branch**.
2. In the terminal:
   ```bash
   git pull
   pip install -r requirements.txt
   ```
