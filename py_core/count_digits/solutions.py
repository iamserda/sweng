"""Given a number, returns the number of digits in num"""


def count_digits(num: int) -> int:
    """Given a number, returns the number of digits in num"""
    count = 0
    while abs(num) > 0:
        num = int(num / 10)
        count += 1
    return count


# TESTS ARENA:
# DO NOT MAKE ANY CHANGE TO THE CODE BELOW...
assert count_digits(-12345) == 5
assert count_digits(1234) == 4
assert count_digits(-45) == 2
assert count_digits(4) == 1
