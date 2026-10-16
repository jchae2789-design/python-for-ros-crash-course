# Week 1 checkpoint: Robot console tools

This is your end-of-week project. It uses **everything** from Week 1: printing, input, numbers, `if`, loops and strings.

You build two small programs:

1. [`converter.py`](converter.py): a unit converter with a menu
2. [`guess.py`](guess.py): a number-guessing game

After completing both programs, in the VS Code terminal, type this test command: You are done when the result is `11 passed`:

```bash
pytest checkpoints/week1
```

Then, in the VS Code terminal, run `python3 checkpoints/week1/converter.py`. Enter the converter's example inputs below.
Type `q` at `Choose:` to return to the VS Code terminal.

Next, in the VS Code terminal, run `python3 checkpoints/week1/guess.py`. Play the game and show both programs to your mentor.
The secret is random, so your guesses can differ from the example.

---

## Part 1: `converter.py`

Robots use many units. Sensor data often comes in one unit and ROS needs another. For example, ROS always uses **meters** and **radians**.

### Step 1: the four conversion functions

First, open [`converter.py`](converter.py) in the VS Code editor. Press **Ctrl + P**.
Type `checkpoints/week1/converter.py` and press Enter. The starter file opens in the editor. Or click [`checkpoints`](../) → [`week1`](./) → [`converter.py`](converter.py) in the file list on the left (Explorer) in the VS Code editor.

In the VS Code editor, read the comments in `converter.py`. Replace `pass` in each conversion function with code that returns the value described below.
Keep the function names and parameters. Save `converter.py` in the VS Code editor with **Ctrl + S**.
The **●** on the file tab disappears.

| Function | Formula | Example |
|---|---|---|
| `c_to_f(c)` | `c * 9 / 5 + 32` | `c_to_f(100)` returns `212.0` |
| `f_to_c(f)` | `(f - 32) * 5 / 9` | `f_to_c(32)` returns `0.0` |
| `mm_to_m(mm)` | `mm / 1000` | `mm_to_m(1500)` returns `1.5` |
| `deg_to_rad(deg)` | `deg * math.pi / 180` | `deg_to_rad(180)` returns `3.14159...` |

`math.pi` comes from the `math` module. The starter file already has `import math` at the top.

### Step 2: the menu in `main()`

In the VS Code editor, replace `pass` inside `main()` in `converter.py`. Write a loop that performs the actions below in order until `q`.
Save `converter.py` in the VS Code editor with **Ctrl + S** before running the program.
These are your program's actions, not terminal commands:

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
- In `main()`, use `float(input("Value: "))` so decimal values like `36.6` also work.

---

## Part 2: `guess.py`

### Step 1: `check_guess(secret, guess)`

First, open [`guess.py`](guess.py) in the VS Code editor. Press **Ctrl + P**.
Type `checkpoints/week1/guess.py` and press Enter. The starter file opens in the editor. Or click [`checkpoints`](../) → [`week1`](./) → [`guess.py`](guess.py) in the file list on the left (Explorer) in the VS Code editor.

In the VS Code editor, read the comments in `guess.py`. Replace `pass` inside `check_guess(secret, guess)` with code that returns the values below.
Keep the function name and parameters. Save `guess.py` in the VS Code editor with **Ctrl + S**.
The **●** on the file tab disappears.

Return:
- `"Too low"` if guess is smaller than secret
- `"Too high"` if guess is bigger than secret
- `"Correct!"` if they are equal

### Step 2: the game in `main()`

In the VS Code editor, replace `pass` inside `main()` in `guess.py`. Write code that performs the actions below in order.
Save `guess.py` in the VS Code editor with **Ctrl + S** before running the program.
These are your program's actions, not terminal commands.

1. Pick a secret number: `secret = random.randint(1, 100)`
2. Repeat:
   - Ask `Your guess: `
   - If the text is not a number (hint: `.isdigit()`), print `Please enter a number.` and ask again. **Do not count this as a try.**
   - Otherwise turn the guess text into an `int`, count one try, and print the result of `check_guess(secret, guess)`.
   - If `check_guess(secret, guess)` returned `"Correct!"`, print `You got it in N tries!` (N is the number of tries) and stop.

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

- In [`converter.py`](converter.py), add these options to the menu in `main()`: `5) Meters -> Millimeters` and `6) Radians -> Degrees`.
- In [`guess.py`](guess.py), let the player choose the range first, for example 1 to 1000.
- In `guess.py`, after the game, ask `Play again? (y/n)`.
