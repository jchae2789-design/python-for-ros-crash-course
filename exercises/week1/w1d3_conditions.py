# Week 1, Day 3: Decisions with if / elif / else
#
# Each exercise is a function. Write your code inside the function and
# use `return` to give back the answer. Replace `pass` with your code.
#
# Test it:  pytest exercises/week1/tests/test_w1d3.py


def battery_status(percent):
    """Return a status word for a battery level.

    - below 0 or above 100   -> "INVALID"
    - 90 or more             -> "FULL"
    - 40 or more             -> "OK"
    - 15 or more             -> "LOW"
    - anything lower         -> "CRITICAL"

    Example: battery_status(55) returns "OK"
    """
    # TODO
    pass


def can_launch(battery_percent, wind_speed, gps_ok):
    """Return True if a drone may take off, otherwise False.

    All three must be true:
    - battery_percent is 30 or more
    - wind_speed (m/s) is 8.0 or less
    - gps_ok is True

    Example: can_launch(80, 3.5, True) returns True
    """
    # TODO
    pass


def classify_distance(distance_m):
    """Decide what a robot does when its LiDAR sees an obstacle.

    - closer than 0.5 m    -> "STOP"
    - closer than 2.0 m    -> "SLOW"
    - otherwise            -> "GO"

    Example: classify_distance(1.2) returns "SLOW"
    """
    # TODO
    pass
