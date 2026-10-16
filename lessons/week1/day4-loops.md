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

Open `exercises/week1/w1d4_loops.py`. There are four functions.

Tip for `steps_until_low`: draw a table like in section 2 with pen and paper for the example `steps_until_low(100, 10, 50)` before you write code.

```bash
pytest exercises/week1/tests/test_w1d4.py
```

---

## 9. Before you finish today

- [ ] `pytest exercises/week1/tests/test_w1d4.py` shows **16 passed**
- [ ] I can say which numbers `range(2, 8, 2)` gives without running it
- [ ] I know how to stop a program that never ends
- [ ] Daily log written, committed and pushed

**Next:** [Day 5: Working with text + checkpoint](day5-strings-and-checkpoint.md)
