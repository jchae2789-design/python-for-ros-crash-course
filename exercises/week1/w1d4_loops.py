# 1주차 4일차: for 문과 while 문으로 반복하기
#
# 각 함수의 `pass`를 코드로 바꾸세요.
#
# 테스트(VS Code 터미널): `pytest exercises/week1/tests/test_w1d4.py`


def countdown(n):
    """n부터 1까지 거꾸로 센 뒤 "GO!"가 붙는 문자열을 반환하세요.

    숫자는 공백 한 칸으로 구분해요.

    예:
        countdown(3)은 "3 2 1 GO!"를 반환해요
        countdown(0)은 "GO!"를 반환해요

    힌트: 빈 문자열로 시작해서 for 문 안에서 내용을 붙이세요.
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def sum_to(n):
    """1 + 2 + ... + n을 반환하세요. 공식 대신 반복문을 사용하세요.

    예:
        sum_to(4)는 10을 반환해요
        sum_to(0)은 0을 반환해요
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def steps_until_low(battery, drain_per_step, low_level):
    """로봇은 한 단계마다 배터리를 `drain_per_step`만큼 사용해요.

    배터리가 `low_level` 이하가 될 때까지 몇 단계가 걸리는지 세세요.
    while 문을 사용하세요.

    예:
        steps_until_low(100, 10, 50)은 5를 반환해요   (100 -> 90 -> 80 -> 70 -> 60 -> 50)
        steps_until_low(100, 7, 20)은 12를 반환해요
        steps_until_low(10, 5, 20)은 0을 반환해요     (이미 기준 이하예요)
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass


def count_multiples(limit, k):
    """1부터 limit까지(limit 포함) 중 k로 나누어떨어지는 숫자의 개수를 세세요.

    예: count_multiples(10, 3)은 3을 반환해요   (3, 6, 9예요)

    힌트: x % k == 0은 x가 k로 나누어떨어진다는 뜻이에요.
    """
    # TODO: 이 줄 아래에 코드를 작성하세요
    pass
