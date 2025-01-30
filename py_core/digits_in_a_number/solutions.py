"""
Given some integer x, return a list of each of its digits.
"""


def digit_in_number(num: int) -> list[int]:
    """Given some integer x, return a list of each of its digits."""
    result = []
    if isinstance(num, int):
        while num > 0:
            result.append(num % 10)
            num = num // 10
        result.reverse()
        return result
    # RAINY DAY
    return []


assert digit_in_number(12345) == [1, 2, 3, 4, 5]
