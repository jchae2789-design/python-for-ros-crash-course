# 1주차 5일차: 문자열 다루기
#
# 각 함수의 `pass`를 코드로 바꾸세요.
#
# 테스트(VS Code 터미널): `pytest exercises/week1/tests/test_w1d5.py`


def clean_command(text):
    """양 끝의 공백과 줄바꿈을 없애고 소문자로 바꾸세요.

    예: clean_command("  FORWARD \n")는 "forward"를 반환해요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def make_topic_name(robot_name, sensor):
    """ROS 방식의 토픽 이름을 만드세요.

    규칙: 모두 소문자로 바꾸고, 공백을 "_"로 바꾸고,
    "/<robot>/<sensor>" 형태로 이어 붙이세요.

    예: make_topic_name("Rail Robot 1", "LiDAR")는 "/rail_robot_1/lidar"를 반환해요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def is_valid_robot_id(robot_id):
    """robot_id가 "RR-0042" 형태이면 True, 아니면 False를 반환하세요.

    올바른 식별 번호는 다음과 같아요.
    - 길이가 정확히 7글자예요
    - 대문자 두 개로 시작해요
    - 세 번째 글자는 "-"예요
    - 숫자 네 개로 끝나요

    예:
        is_valid_robot_id("RR-0042")는 True를 반환해요
        is_valid_robot_id("rr-0042")는 False를 반환해요
        is_valid_robot_id("RR0042")는 False를 반환해요

    힌트: len(), robot_id[0:2] 같은 슬라이싱,
          .isalpha(), .isupper(), .isdigit() 메서드를 사용하세요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def count_char(text, ch):
    """text 안에 글자 ch가 몇 번 나오는지 세세요.

    문자열을 순회하는 for 문을 사용하세요(.count()는 사용하지 마세요).

    예: count_char("rail robot", "o")는 2를 반환해요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass
