# Python for ROS: 4-week crash course

Welcome! This course teaches you Python from zero, step by step, in 4 weeks. After it, you will be ready to program real robots with **ROS 2** (Robot Operating System).

You study **on your own**, at your own pace. Your mentor checks in with you every day. Every exercise has **automatic tests** that tell you when your code is right.

---

## Start here

1. **Set up your computer:** follow [docs/00-setup.md](docs/00-setup.md) (about 1–2 hours).
2. **Learn how to study in this course:** read [docs/01-how-to-study.md](docs/01-how-to-study.md) (10 minutes).
3. **Start Week 1, Day 1:** [lessons/week1/day1-terminal-and-first-program.md](lessons/week1/day1-terminal-and-first-program.md)

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

## Your daily routine

```
Morning     Read today's lesson. Type every example yourself (do not copy-paste).
Afternoon   Solve the exercises. Run the tests until they pass.
Check-in    15 minutes with your mentor. Show your work, ask your questions.
End of day  Write your daily log, then commit and push.
```

Friday: the week's **checkpoint** must pass its tests before you start the next week.

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
```

## Useful commands

```bash
pytest exercises/week1/tests/test_w1d3.py   # test one day
pytest exercises/week1                      # test the whole week
pytest checkpoints/week1                    # test the checkpoint
pytest                                      # test everything
```
