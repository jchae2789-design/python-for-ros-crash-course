# Week 1, Day 5: Working with text (strings)
#
# Replace `pass` with your code in each function.
#
# Test it:  pytest exercises/week1/tests/test_w1d5.py


def clean_command(text):
    """Remove spaces/newlines at both ends and make it lowercase.

    Example: clean_command("  FORWARD \n") returns "forward"
    """
    # TODO
    pass


def make_topic_name(robot_name, sensor):
    """Build a ROS-style topic name.

    Rules: lowercase everything, replace spaces with "_", and join as
    "/<robot>/<sensor>".

    Example: make_topic_name("Rail Robot 1", "LiDAR") returns "/rail_robot_1/lidar"
    """
    # TODO
    pass


def is_valid_robot_id(robot_id):
    """Return True if robot_id looks like "RR-0042", otherwise False.

    A valid id:
    - is exactly 7 characters long
    - starts with 2 uppercase letters
    - has "-" as the 3rd character
    - ends with 4 digits

    Examples:
        is_valid_robot_id("RR-0042") returns True
        is_valid_robot_id("rr-0042") returns False
        is_valid_robot_id("RR0042")  returns False

    Hints: len(), slicing like robot_id[0:2], and the methods
           .isalpha(), .isupper(), .isdigit()
    """
    # TODO
    pass


def count_char(text, ch):
    """Count how many times the character ch appears in text.

    Use a for loop over the text (do not use .count()).

    Example: count_char("rail robot", "o") returns 2
    """
    # TODO
    pass
