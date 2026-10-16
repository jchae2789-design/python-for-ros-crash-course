# Week 1, Day 4: Repeating with for and while
#
# Replace `pass` with your code in each function.
#
# Test it:  pytest exercises/week1/tests/test_w1d4.py


def countdown(n):
    """Return a countdown text from n down to 1, then "GO!".

    Numbers are separated by single spaces.

    Examples:
        countdown(3) returns "3 2 1 GO!"
        countdown(0) returns "GO!"

    Hint: start with an empty text and add to it inside a for loop.
    """
    # TODO
    pass


def sum_to(n):
    """Return 1 + 2 + ... + n. Use a loop (no formula).

    Examples:
        sum_to(4) returns 10
        sum_to(0) returns 0
    """
    # TODO
    pass


def steps_until_low(battery, drain_per_step, low_level):
    """A robot loses `drain_per_step` battery every step.

    Count how many steps it takes until the battery is at `low_level`
    or below. Use a while loop.

    Examples:
        steps_until_low(100, 10, 50) returns 5   (100 -> 90 -> 80 -> 70 -> 60 -> 50)
        steps_until_low(100, 7, 20) returns 12
        steps_until_low(10, 5, 20) returns 0     (already low)
    """
    # TODO
    pass


def count_multiples(limit, k):
    """Count the numbers from 1 to limit (inclusive) that k divides evenly.

    Example: count_multiples(10, 3) returns 3   (3, 6 and 9)

    Hint: x % k == 0 means k divides x evenly.
    """
    # TODO
    pass
