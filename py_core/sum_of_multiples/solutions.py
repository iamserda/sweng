"""Given an integer, and some number x, return the sums of digits that are multiples of x."""


def sum_of_multiples_of(x, num):
    """Given an integer, and sum number x, return the sums of digits that are multiples of x."""
    result = 0
    if not x:
        return None

    while num > 0:
        n = num % 10
        if n % x == 0:
            result += n
        num //= 10
    return result


# Tests Arena
assert sum_of_multiples_of(2, 123456789) == 20
assert sum_of_multiples_of(3, 3567) == 9
assert sum_of_multiples_of(0, 2468) is None
assert sum_of_multiples_of(10, 2468) == 0
