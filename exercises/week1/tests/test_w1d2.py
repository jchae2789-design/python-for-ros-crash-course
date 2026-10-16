from pathlib import Path

import pytest

HERE = Path(__file__).parent.parent


@pytest.mark.parametrize(
    "capacity, current, expected",
    [
        ("5000", "2000", "Runtime: 2.50 hours"),
        ("3300", "1100", "Runtime: 3.00 hours"),
        ("1000", "3000", "Runtime: 0.33 hours"),
    ],
)
def test_battery_runtime(run_script, capacity, current, expected):
    output = run_script(HERE / "w1d2_battery_runtime.py", f"{capacity}\n{current}\n")
    assert expected in output, (
        f"With {capacity} mAh and {current} mA we expected {expected!r}.\n"
        f"Your program printed: {output!r}"
    )


@pytest.mark.parametrize(
    "seconds, expected",
    [
        ("3725", "1 h 2 m 5 s"),
        ("59", "0 h 0 m 59 s"),
        ("7200", "2 h 0 m 0 s"),
    ],
)
def test_time_format(run_script, seconds, expected):
    output = run_script(HERE / "w1d2_time_format.py", f"{seconds}\n")
    assert expected in output, (
        f"For {seconds} seconds we expected {expected!r}.\n"
        f"Your program printed: {output!r}"
    )
