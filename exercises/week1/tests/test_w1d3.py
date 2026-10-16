import pytest

from w1d3_conditions import battery_status, can_launch, classify_distance


@pytest.mark.parametrize(
    "percent, expected",
    [
        (100, "FULL"), (90, "FULL"), (89, "OK"), (40, "OK"),
        (39, "LOW"), (15, "LOW"), (14, "CRITICAL"), (0, "CRITICAL"),
        (-1, "INVALID"), (101, "INVALID"),
    ],
)
def test_battery_status(percent, expected):
    assert battery_status(percent) == expected


@pytest.mark.parametrize(
    "battery, wind, gps, expected",
    [
        (80, 3.5, True, True),
        (30, 8.0, True, True),
        (29, 3.0, True, False),
        (80, 8.1, True, False),
        (80, 3.0, False, False),
    ],
)
def test_can_launch(battery, wind, gps, expected):
    assert can_launch(battery, wind, gps) is expected


@pytest.mark.parametrize(
    "distance, expected",
    [(0.1, "STOP"), (0.49, "STOP"), (0.5, "SLOW"), (1.99, "SLOW"), (2.0, "GO"), (10, "GO")],
)
def test_classify_distance(distance, expected):
    assert classify_distance(distance) == expected
