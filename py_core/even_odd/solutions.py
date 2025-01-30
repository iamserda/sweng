def is_even(some_number):
    return some_number % 2 == 0


def is_odd(some_number):
    return not is_even(some_number)
# Tests Arena


assert is_even(-5) is False
assert is_even(4) is True
assert is_odd(-4) is False
assert is_odd(5) is True
