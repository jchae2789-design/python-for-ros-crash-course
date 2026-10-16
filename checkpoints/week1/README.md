# Week 1 checkpoint: Robot console tools

This is your end-of-week project. It uses **everything** from Week 1: printing, input, numbers, `if`, loops and strings.

You build two small programs:

1. `converter.py`: a unit converter with a menu
2. `guess.py`: a number-guessing game

You are done when these tests pass:

```bash
pytest checkpoints/week1
```

Then show your mentor both programs running in the terminal.

---

## Part 1: `converter.py`

Robots use many units. Sensor data often comes in one unit and ROS needs another. For example, ROS always uses **meters** and **radians**.

### Step 1: the four conversion functions

| Function | Formula | Example |
|---|---|---|
| `c_to_f(c)` | `c * 9 / 5 + 32` | `c_to_f(100)` returns `212.0` |
| `f_to_c(f)` | `(f - 32) * 5 / 9` | `f_to_c(32)` returns `0.0` |
| `mm_to_m(mm)` | `mm / 1000` | `mm_to_m(1500)` returns `1.5` |
| `deg_to_rad(deg)` | `deg * math.pi / 180` | `deg_to_rad(180)` returns `3.14159...` |

`math.pi` comes from the `math` module. The starter file already has `import math` at the top.

### Step 2: the menu in `main()`

`main()` repeats this until the user types `q`:

1. Print the menu:
   ```
   === Unit Converter ===
   1) Celsius -> Fahrenheit
   2) Fahrenheit -> Celsius
   3) Millimeters -> Meters
   4) Degrees -> Radians
   q) Quit
   ```
2. Ask `Choose: `
3. If the choice is `q`, print `Bye!` and stop the loop.
4. If the choice is `1`, `2`, `3` or `4`, ask `Value: `, convert with the right function and print the result with 2 decimals: `Result: 212.00`
5. For any other choice, print `Unknown choice.`

Example session (what you type comes after `Choose:` and `Value:`):

```
=== Unit Converter ===
...
Choose: 1
Value: 100
Result: 212.00
=== Unit Converter ===
...
Choose: 7
Unknown choice.
=== Unit Converter ===
...
Choose: q
Bye!
```

Hints:
- `while True:` with `break` is a good fit for "repeat until q".
- Use `float(input("Value: "))` so that decimal values like `36.6` also work.

---

## Part 2: `guess.py`

### Step 1: `check_guess(secret, guess)`

Return:
- `"Too low"` if guess is smaller than secret
- `"Too high"` if guess is bigger than secret
- `"Correct!"` if they are equal

### Step 2: the game in `main()`

1. Pick a secret number: `secret = random.randint(1, 100)`
2. Repeat:
   - Ask `Your guess: `
   - If the text is not a number (hint: `.isdigit()`), print `Please enter a number.` and ask again. **Do not count this as a try.**
   - Otherwise turn it into an `int`, count one try, and print the result of `check_guess`.
   - If it was correct, print `You got it in N tries!` (N is the number of tries) and stop.

Example session (secret is 42):

```
Your guess: 50
Too high
Your guess: abc
Please enter a number.
Your guess: 25
Too low
Your guess: 42
Correct!
You got it in 3 tries!
```

---

## Bonus (not tested)

- Converter: add `5) Meters -> Millimeters` and `6) Radians -> Degrees`.
- Guess: let the player choose the range first, for example 1 to 1000.
- Guess: after the game, ask `Play again? (y/n)`.
