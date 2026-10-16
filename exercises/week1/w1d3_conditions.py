# 1주차 3일차: if / elif / else로 판단하기
#
# 각 연습 문제는 함수예요. 함수 안에 코드를 작성하고
# `return`으로 답을 반환하세요. `pass`를 코드로 바꾸세요.
#
# 테스트(VS Code 터미널): `pytest exercises/week1/tests/test_w1d3.py`


def battery_status(percent):
    """배터리 잔량에 맞는 상태 단어를 반환하세요.

    - 0 미만 또는 100 초과   -> "INVALID"
    - 90 이상                -> "FULL"
    - 40 이상                -> "OK"
    - 15 이상                -> "LOW"
    - 그보다 작은 값         -> "CRITICAL"

    예: battery_status(55)는 "OK"를 반환해요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def can_launch(battery_percent, wind_speed, gps_ok):
    """드론이 이륙해도 되면 True, 아니면 False를 반환하세요.

    세 조건이 모두 참이어야 해요.
    - battery_percent가 30 이상이에요
    - wind_speed(m/s)가 8.0 이하예요
    - gps_ok가 True예요

    예: can_launch(80, 3.5, True)는 True를 반환해요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def classify_distance(distance_m):
    """라이다가 장애물을 감지했을 때 로봇이 할 일을 결정하세요.

    - 거리가 0.5 m 미만   -> "STOP"
    - 거리가 2.0 m 미만   -> "SLOW"
    - 그 밖의 경우        -> "GO"

    예: classify_distance(1.2)는 "SLOW"를 반환해요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass
