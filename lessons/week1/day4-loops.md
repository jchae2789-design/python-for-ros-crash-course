# Week 1 · Day 4: Repeating: `for` and `while` loops

**You will learn:** how to repeat code a fixed number of times (`for`), how to repeat until something changes (`while`), and how to stop or skip in a loop.

**Why this matters for robots:** a robot program is one big loop: *read sensors → decide → move → repeat*, many times per second. In ROS this loop is hidden inside `rclpy.spin()`, but it is still a loop.

---

## 1. `for` with `range()`

```python
for i in range(5):
    print("Reading sensor", i)
```

```
Reading sensor 0
Reading sensor 1
Reading sensor 2
Reading sensor 3
Reading sensor 4
```

- `range(5)` gives the numbers `0, 1, 2, 3, 4`. **It starts at 0 and stops before 5.**
- Each time through the loop, `i` gets the next number.
- The indented lines run once for each number.

### More forms of `range`

| Code | Numbers |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 (steps of 2) |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 (counting down) |

The stop value is **never** included. To go up to `n`, write `range(1, n + 1)`.

### Try it

In `playground.py`, write a loop that prints numbers from 10 down to 0 in steps of 2.
Save with **Ctrl + S**. Run `python3 playground.py` in the terminal. Expected numbers: `10 8 6 4 2 0` (one per line is fine).

---

## 2. The accumulator pattern

A very common job: go through many values and build **one** result. Start with an empty result **before** the loop and update it **inside** the loop:

```python
total = 0                    # 1. start value, before the loop
for i in range(1, 4):
    total = total + i        # 2. update inside the loop
print(total)                 # 3. use it after the loop → 6
```

Step by step:

| Round | `i` | `total` after |
|---|---|---|
| start | | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |

The same pattern works for **counting**:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:           # only even numbers
        count = count + 1
print(count)                 # 5
```

And for **building text**:

```python
text = ""
for i in range(3):
    text = text + "beep "
print(text)                  # "beep beep beep "
```

Use `str(i)` to add a number to a text: `text = text + str(i)`.

> **Shortcut:** `total += i` means the same as `total = total + i`. Both are fine.

---

## 3. `while`: repeat as long as a condition is True

Use `while` when you do **not** know in advance how many times to repeat.

```python
battery = 100
while battery > 20:
    print(f"Working... battery {battery}%")
    battery = battery - 30
print("Going to charger")
```

```
Working... battery 100%
Working... battery 70%
Working... battery 40%
Going to charger
```

Before each round, Python checks the condition. When it is `False`, the loop ends.

⚠️ **Something inside the loop must change the condition.** Otherwise the loop runs forever:

```python
battery = 100
while battery > 20:
    print("Working...")      # battery never changes → never ends!
```

If the `while battery > 20` loop prints `Working...` forever, press **Ctrl + C** in the terminal to stop the program.

---

## 4. `break` and `continue`

- `break` leaves the loop **immediately**.
- `continue` skips the rest of this round and starts the **next** round.

A common pattern: loop forever and `break` when you are done. This is how menu programs work (you will need it for the checkpoint!):

```python
while True:
    command = input("Command (q to quit): ")
    if command == "q":
        break
    print("Running", command)
print("Bye")
```

`continue` example: skip bad sensor readings:

```python
for reading in range(-2, 4):
    if reading < 0:
        continue             # negative = sensor error, skip it
    print("Valid reading:", reading)
```

---

## 5. Loops inside functions

```python
def count_even(limit):
    count = 0
    for i in range(1, limit + 1):
        if i % 2 == 0:
            count = count + 1
    return count             # after the loop, not inside it!


print(count_even(10))        # 5
```

⚠️ Watch the indentation of `return`. If you indent it into the loop, the function stops after the first round.

---

## 6. `for` or `while`?

| Use | When | Example |
|---|---|---|
| `for` | you know how many times | "check 10 sensors", "count from 1 to n" |
| `while` | you repeat until something happens | "until battery is low", "until the user types q" |

---

## 7. Common mistakes

| Mistake | Fix |
|---|---|
| Loop runs one time too few | `range` stops **before** the end value: use `range(1, n + 1)` |
| Program never ends | `while` condition never becomes False. Press **Ctrl + C** in the terminal, then edit the loop in `playground.py` in VS Code so the condition variable changes |
| Result is always 0 or wrong | The start value (`total = 0`) is inside the loop, so it is reset every round. In VS Code, move `total = 0` **before** the loop in `playground.py` |
| Function returns after the first round | `return` is indented inside the loop. In VS Code, move `return` outside the loop in the function you are editing |

---

## 8. Exercises

**How to do the exercises:** do them **in order**, one at a time. Each exercise below has numbered steps. Follow them from 1 to the end, then go to the next exercise. If a step does not work, look at [How exercises work, Part 5](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

All four functions are in [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py). Follow the numbered steps for each function below.

### Exercise 1 of 4: `countdown(n)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** return a text that counts down from `n` to 1, then `GO!`, separated by spaces.

```python
>>> countdown(3)
'3 2 1 GO!'
>>> countdown(0)
'GO!'
```

**Example to follow:** a similar problem (not the answer to this exercise).

This function counts **up** instead of down and ends with `DONE`. For your exercise, think about which `range(...)` counts **down** (section 1).

```python
def count_up(n):
    text = ""
    for i in range(1, n + 1):
        text = text + str(i) + " "
    return text + "DONE"
```

Try the example: open `playground.py` with `code playground.py`.
Type the example in VS Code. Save with **Ctrl + S**.
Run `python3 -i playground.py` in the terminal.

At `>>>`, type the calls below. The lines without `>>>` are the results you should see:

```python
$ python3 -i playground.py
>>> count_up(3)
'1 2 3 DONE'
>>> count_up(0)
'DONE'
>>> exit()
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, press **Ctrl + P**.
   Type [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py) and press Enter. The file opens in the editor.
2. Replace `pass` inside `countdown` with your code. Use the "building text" pattern from section 2. Start with `text = ""`.
   Add numbers inside a `for` loop with a counting-down `range` (section 1).
   Add `"GO!"` at the end. Use `str(i)` to turn a number into text.
3. Save with **Ctrl + S**. The **●** on the file tab disappears.

   In the terminal, run `python3 -i exercises/week1/w1d4_loops.py`.
   At `>>>`, type the `countdown(...)` calls under **Your task** above. Compare the results.

   Type `exit()` at `>>>` to return to the terminal.
4. Test `countdown` with [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py):
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k countdown
   ```
   ✔ You should see `4 passed, 12 deselected`.
5. In VS Code, open [`progress/week1.md`](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `countdown`. Save with **Ctrl + S**.

> `deselected` means: the tests of the **other** exercises in this file were not run. That is what `-k` does, and it is fine.

### Exercise 2 of 4: `sum_to(n)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** return 1 + 2 + … + n, using a loop.

```python
>>> sum_to(4)
10
>>> sum_to(0)
0
```

**Example to follow:** a similar problem (not the answer to this exercise).

This function **multiplies** 1 × 2 × … × n. Notice it starts at `1`, not `0`. Anything times 0 is 0! For a sum, think about which start value is right.

```python
def product_to(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
```

Try the example: open `playground.py` with `code playground.py`.
Type the example in VS Code. Save with **Ctrl + S**.
Run `python3 -i playground.py` in the terminal.

At `>>>`, type the calls below. The lines without `>>>` are the results you should see:

```python
$ python3 -i playground.py
>>> product_to(4)
24
>>> product_to(0)
1
>>> exit()
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, press **Ctrl + P**.
   Type [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py) and press Enter. The file opens in the editor.
2. Replace `pass` inside `sum_to` with your code. This is exactly the accumulator pattern in section 2. Remember: to include `n`, use `range(1, n + 1)`.
3. Save with **Ctrl + S**. The **●** on the file tab disappears.

   In the terminal, run `python3 -i exercises/week1/w1d4_loops.py`.
   At `>>>`, type the `sum_to(...)` calls under **Your task** above. Compare the results.

   Type `exit()` at `>>>` to return to the terminal.
4. Test `sum_to` with [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py):
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k sum_to
   ```
   ✔ You should see `4 passed, 12 deselected`.
5. In VS Code, open [`progress/week1.md`](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `sum_to`. Save with **Ctrl + S**.

### Exercise 3 of 4: `steps_until_low(battery, drain_per_step, low_level)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** each step, the robot loses `drain_per_step` battery. Return how many steps it takes until the battery is at `low_level` or below.

```python
>>> steps_until_low(100, 10, 50)
5
>>> steps_until_low(10, 5, 20)
0
```

**Example to follow:** a similar problem (not the answer to this exercise).

This function is the opposite of your exercise: it **charges** a battery until it is full, and counts the steps with a `while` loop.

```python
def steps_until_full(battery, charge_per_step, full_level):
    steps = 0
    while battery < full_level:
        battery = battery + charge_per_step
        steps = steps + 1
    return steps
```

Try the example: open `playground.py` with `code playground.py`.
Type the example in VS Code. Save with **Ctrl + S**.
Run `python3 -i playground.py` in the terminal.

At `>>>`, type the calls below. The lines without `>>>` are the results you should see:

```python
$ python3 -i playground.py
>>> steps_until_full(50, 10, 100)
5
>>> steps_until_full(100, 10, 100)
0
>>> exit()
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, press **Ctrl + P**.
   Type [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py) and press Enter. The file opens in the editor.
2. **First, on paper:** draw a table like in section 2 for `steps_until_low(100, 10, 50)`, with columns *step* and *battery*. Count until the battery is 50 or below. You should get 5.
3. Replace `pass` inside `steps_until_low` with your code. Use a `while` loop (section 3): keep going **while** the battery is above `low_level`. Inside, subtract the drain and add 1 to a step counter.
4. Save with **Ctrl + S**. The **●** on the file tab disappears.

   In the terminal, run `python3 -i exercises/week1/w1d4_loops.py`.
   At `>>>`, type the `steps_until_low(...)` calls under **Your task** above. Compare the results.

   Type `exit()` at `>>>` to return to the terminal. If the `steps_until_low(...)` call never finishes, press **Ctrl + C** in the terminal: your battery is not going down.
5. Test `steps_until_low` with [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py):
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k steps_until_low
   ```
   ✔ You should see `4 passed, 12 deselected`.
6. In VS Code, open [`progress/week1.md`](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `steps_until_low`. Save with **Ctrl + S**.

### Exercise 4 of 4: `count_multiples(limit, k)`

> 📖 **Before you start:** open [How exercises work](../../docs/02-how-exercises-work.md) next to this lesson.
> Follow [Part 4: a function exercise](../../docs/02-how-exercises-work.md#part-4-worked-example-a-function-exercise-days-35) and [Part 5: reading test results](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

**Your task:** count the numbers from 1 to `limit` (including `limit`) that `k` divides evenly.

```python
>>> count_multiples(10, 3)
3
```

(3, 6 and 9.)

**Example to follow:** a similar problem (not the answer to this exercise).

This function counts the **odd** numbers from 1 to `limit`. An odd number has remainder 1 when divided by 2.

```python
def count_odd(limit):
    count = 0
    for x in range(1, limit + 1):
        if x % 2 == 1:
            count = count + 1
    return count
```

Try the example: open `playground.py` with `code playground.py`.
Type the example in VS Code. Save with **Ctrl + S**.
Run `python3 -i playground.py` in the terminal.

At `>>>`, type the calls below. The lines without `>>>` are the results you should see:

```python
$ python3 -i playground.py
>>> count_odd(10)
5
>>> count_odd(1)
1
>>> exit()
```

When you understand how the example works, do the steps below. Write your own code for the exercise. Do not copy the example: the task is different.

**Steps:**

1. **Open the file.** In VS Code, press **Ctrl + P**.
   Type [`exercises/week1/w1d4_loops.py`](../../exercises/week1/w1d4_loops.py) and press Enter. The file opens in the editor.
2. Replace `pass` inside `count_multiples` with your code. Loop over 1 to `limit` and count the numbers where `x % k == 0`. This is the counting example in section 2.
3. Save with **Ctrl + S**. The **●** on the file tab disappears.

   In the terminal, run `python3 -i exercises/week1/w1d4_loops.py`.
   At `>>>`, type the `count_multiples(...)` calls under **Your task** above. Compare the results.

   Type `exit()` at `>>>` to return to the terminal.
4. Test `count_multiples` with [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py):
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k count_multiples
   ```
   ✔ You should see `4 passed, 12 deselected`.
5. In VS Code, open [`progress/week1.md`](../../progress/week1.md).
   Change `[ ]` to `[x]` beside `count_multiples`. Save with **Ctrl + S**.

### Finally: all of today's tests

Run today's tests in [`test_w1d4.py`](../../exercises/week1/tests/test_w1d4.py):

```bash
pytest exercises/week1/tests/test_w1d4.py
```

✔ You should see **`16 passed`**. In VS Code, check the Day 4 "Tests pass" box in [`progress/week1.md`](../../progress/week1.md). Save with **Ctrl + S**.

---

## 9. Before you finish today

In VS Code, open [progress/week1.md](../../progress/week1.md). Mark each completed Day 4 box `[x]`.
Save with **Ctrl + S**. Only start Day 5 when every Day 4 box is checked.

- [ ] `pytest exercises/week1/tests/test_w1d4.py` shows **16 passed**
- [ ] I can say which numbers `range(2, 8, 2)` gives without running it
- [ ] I know how to stop a program that never ends
- [ ] Daily log written, committed and pushed

**Next:** [Day 5: Working with text + checkpoint](day5-strings-and-checkpoint.md)
