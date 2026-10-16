from pathlib import Path

HERE = Path(__file__).parent.parent


def test_hello(run_script):
    output = run_script(HERE / "w1d1_hello.py")
    assert output == "Hello, ROS!\n", f"Your program printed: {output!r}"


def test_robot_card(run_script):
    output = run_script(HERE / "w1d1_robot_card.py")
    expected = "Robot: RR-01\nType: Rail robot\nStatus: READY\n"
    assert output == expected, f"Your program printed:\n{output}"
