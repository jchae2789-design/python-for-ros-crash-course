# Python for ROS: 4-week crash course

Welcome! This course teaches you Python from zero, step by step, in 4 weeks. After it, you will be ready to program real robots with **ROS 2** (Robot Operating System).

You study **on your own**, at your own pace. Your mentor checks in with you every day. Every exercise has **automatic tests** that tell you when your code is right.

---

## Start here

👉 **Open [progress/week1.md](progress/week1.md) and follow it from top to bottom.**

It is your checklist for the whole week: setup, reading, every lesson and exercise, in the right order. Check off each step yourself when it is done, and only move on when everything above is checked.

The first steps on the checklist are:

1. **Set up your computer:** [docs/00-setup.md](docs/00-setup.md) (about 1–2 hours)
2. **Learn how to study in this course:** [docs/01-how-to-study.md](docs/01-how-to-study.md) (10 minutes)
3. **Learn how exercises and tests work:** [docs/02-how-exercises-work.md](docs/02-how-exercises-work.md) (20 minutes)
4. **Week 1, Day 1:** [lessons/week1/day1-terminal-and-first-program.md](lessons/week1/day1-terminal-and-first-program.md)

---

## Schedule

| Week | Dates (2026) | Topic | Why it matters for ROS | Checkpoint |
|---|---|---|---|---|
| **1** | Oct 19 – Oct 23 | Terminal and Python basics | You control ROS from the terminal | Robot console tools (unit converter + guessing game) |
| **2** | Oct 26 – Oct 30 | Data and functions | ROS messages are structured data | Sensor data analyzer |
| **3** | Nov 2 – Nov 6 | Organizing code: classes, modules, errors | Every ROS node is a class | Robot class family |
| **4** | Nov 9 – Nov 13 | ROS-style patterns: callbacks, timers, publish/subscribe | Same ideas as real ROS 2 | **mini-ROS**: build your own tiny ROS |

Weeks 2–4 will appear in this repository when you are ready for them. See [Getting new lessons](docs/01-how-to-study.md#getting-new-lessons).

### Week 1

| Day | Lesson | Exercises |
|---|---|---|
| 1 | [Terminal and your first program](lessons/week1/day1-terminal-and-first-program.md) | `exercises/week1/w1d1_*.py` |
| 2 | [Variables, numbers and input](lessons/week1/day2-variables-numbers-input.md) | `exercises/week1/w1d2_*.py` |
| 3 | [Making decisions: functions and if](lessons/week1/day3-functions-and-decisions.md) | `exercises/week1/w1d3_conditions.py` |
| 4 | [Repeating: for and while loops](lessons/week1/day4-loops.md) | `exercises/week1/w1d4_loops.py` |
| 5 | [Working with text + checkpoint](lessons/week1/day5-strings-and-checkpoint.md) | `exercises/week1/w1d5_strings.py`, [checkpoint](checkpoints/week1/README.md) |

---

## How to progress through the class

The class is **one path**. You always do the next step, never skip ahead:

```
Setup → Day 1 → Day 2 → Day 3 → Day 4 → Day 5 + checkpoint → Week 2 → ... → Week 4 → ROS 2
```

Your checklist in `progress/` tells you exactly where you are on this path.

### Step 1: Find where you are

Open your checklist for the current week, for example [progress/week1.md](progress/week1.md). **Your next step is the first box that is not checked.**

```markdown
- [x] Read the lesson and typed every example myself
- [x] Did the "Try it" tasks in the lesson
- [ ] Exercise `exercises/week1/w1d1_hello.py`      ← you are here
- [ ] Exercise `exercises/week1/w1d1_robot_card.py`
```

### Step 2: Do that step

Follow the link or instructions in the box. For exercises, see [How exercises work](docs/02-how-exercises-work.md).

### Step 3: Check that it is really done

- **Reading a lesson:** you typed and ran every example.
- **An exercise:** you tried it yourself, and it does what the instructions say.
- **A "Tests pass" box:** run the command in the box. The result must match **exactly**, for example `21 passed`.
- **An "I can explain…" box:** say it out loud without looking. If you can't, read that part of the lesson again.

### Step 4: Check the box

In VS Code, change `[ ]` to `[x]` (lowercase x, no spaces) and save with **Ctrl + S**:

```markdown
- [ ] Exercise `exercises/week1/w1d1_hello.py`      ← before
- [x] Exercise `exercises/week1/w1d1_hello.py`      ← after
```

After you push, GitHub shows the boxes in your checklist as real checkboxes.

Then go back to **Step 1**.

### End of every day

The last boxes of each day are: write your daily log, commit and push, and check in with your mentor. Commit your checklist together with your code:

```bash
git add .
git commit -m "Week 1 Day 1: finished exercises"
git push
```

Your mentor opens your fork on GitHub and sees your checklist, your code, your log, and whether your tests pass (✅ or ❌).

### Moving to the next day

Start **Day N + 1** only when **every box of Day N** is checked. If you finish early, use the time to try the "Bonus" ideas or to re-read the hard parts. Don't start the next day early.

### Moving to the next week

A week is finished when:

1. every box in the week's checklist is checked, including **"Week N done"**,
2. the week's checkpoint passes its tests,
3. you showed the checkpoint to your mentor.

Then get the next week:

1. On GitHub, open your fork and click **Sync fork** → **Update branch**.
2. In the terminal, run `git pull`.
3. Open the new checklist (for example `progress/week2.md`) and start at the first box.

### A normal day

```
Morning     Read today's lesson. Type every example yourself (do not copy-paste).
Afternoon   Solve the exercises. Run the tests until they pass.
Check-in    15 minutes with your mentor. Show your work, ask your questions.
End of day  Write your daily log, check your boxes, commit and push.
```

---

## Rules

- **Type, don't paste.** Your fingers learn too.
- **Try for 20 minutes, then ask.** Being stuck for 20 minutes is normal. Being stuck for 2 hours is a waste. Write the question in your log and ask your mentor.
- **AI tools** (ChatGPT, Claude, Copilot, …): you may ask them to **explain an error message or a concept**. You may **not** ask them to write your exercise or checkpoint code. Your mentor will ask you to explain your code line by line.
- **Push every day.** Your mentor sees your progress on GitHub.
- **Never edit the `tests/` folders.** Change your code until the tests pass, not the other way around.

---

## Repository map

```
README.md           ← you are here
docs/               setup and how-to-study guides
lessons/weekN/      the lessons: read these
exercises/weekN/    your exercise files: write your code here
exercises/weekN/tests/   automatic tests (do not edit)
checkpoints/weekN/  end-of-week projects
logs/               your daily logs (copy TEMPLATE.md)
progress/           your checklists: one per week, follow them in order
```

## Useful commands

```bash
pytest exercises/week1/tests/test_w1d3.py   # test one day
pytest exercises/week1                      # test the whole week
pytest checkpoints/week1                    # test the checkpoint
pytest                                      # test everything
```
