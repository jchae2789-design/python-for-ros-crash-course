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

Print the numbers from 10 down to 0 in steps of 2: `10 8 6 4 2 0` (one per line is fine).

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

If this happens, press **Ctrl + C** in the terminal to stop it.

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
| Program never ends | `while` condition never becomes False. Press Ctrl + C, then make sure the loop changes the variable |
| Result is always 0 or wrong | The start value (`total = 0`) is inside the loop, so it is reset every round. Put it **before** the loop |
| Function returns after the first round | `return` is indented inside the loop. Move it out |

---

## 8. Exercises

**How to do the exercises:** do them **in order**, one at a time. Each exercise below has numbered steps. Follow them from 1 to the end, then go to the next exercise. If a step does not work, look at [How exercises work, Part 5](../../docs/02-how-exercises-work.md#part-5-reading-test-results).

All four functions are in `exercises/week1/w1d4_loops.py`. Open it in VS Code now. For each one: replace `pass`, save, try it with `python3 -i exercises/week1/w1d4_loops.py`, run its tests, then check its box in [progress/week1.md](../../progress/week1.md).

### Exercise 1 of 4: `countdown(n)`

**Your task:** return a text that counts down from `n` to 1, then `GO!`, separated by spaces.

```python
>>> countdown(3)
'3 2 1 GO!'
>>> countdown(0)
'GO!'
```

**Steps:**

1. Replace `pass`. Use the "building text" pattern from section 2: start with `text = ""`, add to it in a `for` loop with a counting-down `range` (section 1), and add `"GO!"` at the end. Use `str(i)` to turn a number into text.
2. Save and try it with `python3 -i`. You should get the results above.
3. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k countdown
   ```
   ✔ You should see `4 passed, 12 deselected`.
4. Check the box for `countdown`.

> `deselected` means: the tests of the **other** exercises in this file were not run. That is what `-k` does, and it is fine.

### Exercise 2 of 4: `sum_to(n)`

**Your task:** return 1 + 2 + … + n, using a loop.

```python
>>> sum_to(4)
10
>>> sum_to(0)
0
```

**Steps:**

1. Replace `pass`. This is exactly the accumulator pattern in section 2. Remember: to include `n`, use `range(1, n + 1)`.
2. Save and try it with `python3 -i`.
3. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k sum_to
   ```
   ✔ You should see `4 passed, 12 deselected`.
4. Check the box for `sum_to`.

### Exercise 3 of 4: `steps_until_low(battery, drain_per_step, low_level)`

**Your task:** each step, the robot loses `drain_per_step` battery. Return how many steps it takes until the battery is at `low_level` or below.

```python
>>> steps_until_low(100, 10, 50)
5
>>> steps_until_low(10, 5, 20)
0
```

**Steps:**

1. **First, on paper:** draw a table like in section 2 for `steps_until_low(100, 10, 50)`, with columns *step* and *battery*. Count until the battery is 50 or below. You should get 5.
2. Replace `pass`. Use a `while` loop (section 3): keep going **while** the battery is above `low_level`. Inside, subtract the drain and add 1 to a step counter.
3. Save and try it with `python3 -i`. If it never finishes, press **Ctrl + C**: your battery is not going down.
4. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k steps_until_low
   ```
   ✔ You should see `4 passed, 12 deselected`.
5. Check the box for `steps_until_low`.

### Exercise 4 of 4: `count_multiples(limit, k)`

**Your task:** count the numbers from 1 to `limit` (including `limit`) that `k` divides evenly.

```python
>>> count_multiples(10, 3)
3
```

(3, 6 and 9.)

**Steps:**

1. Replace `pass`. Loop over 1 to `limit` and count the numbers where `x % k == 0`. This is the counting example in section 2.
2. Save and try it with `python3 -i`.
3. Test it:
   ```bash
   pytest exercises/week1/tests/test_w1d4.py -k count_multiples
   ```
   ✔ You should see `4 passed, 12 deselected`.
4. Check the box for `count_multiples`.

### Finally: all of today's tests

```bash
pytest exercises/week1/tests/test_w1d4.py
```

✔ You should see **`16 passed`**. Check the "Tests pass" box in your checklist.

---

## 9. Before you finish today

Check off **Day 4** in your checklist: [progress/week1.md](../../progress/week1.md). Only start Day 5 when every Day 4 box is checked.

- [ ] `pytest exercises/week1/tests/test_w1d4.py` shows **16 passed**
- [ ] I can say which numbers `range(2, 8, 2)` gives without running it
- [ ] I know how to stop a program that never ends
- [ ] Daily log written, committed and pushed

**Next:** [Day 5: Working with text + checkpoint](day5-strings-and-checkpoint.md)
