""" Given an integer, return its individual digits. Do not convert to str."""
def sum_of_digits(some_number):
    """ Given an integer, return its individual digits."""
    the_sum = None
    if isinstance(some_number, int):
        the_sum = 0
        while some_number != 0:
            remainder_num = some_number % 10
            some_number = some_number // 10
            the_sum += remainder_num
    return the_sum

# Tests Arena:
assert sum_of_digits(12345) == 15
assert sum_of_digits(1) == 1
assert sum_of_digits(345) == 12
assert sum_of_digits(0) == 0

# value = sum_of_digits(12345)
# print(value)
