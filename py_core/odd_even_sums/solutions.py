""" Given an integer, return its individual digits."""


def list_sum(arr: list[int]):
    """given a list of integers,
    return the sum of its digits.
    """
    sum = 0
    for i in arr:
        sum += i
    return sum

def sum_of_odd_and_even(num):
    """ Given an integer, return the sum of its even digits a sum of its odd digits"""

    if not num:
        return

    even = [int(i) for i in str(num) if int(i) % 2 == 0]
    odd = [int(i) for i in str(num) if int(i) % 2 != 0]
    return list_sum(odd), list_sum(even)


# odd, even = sum_of_odd_and_even(1357902468)
# print(f"odd_sum: {odd}, evn_sum: {even}")

# Tests Arena:
assert sum_of_odd_and_even(12345) == (9, 6)
assert sum_of_odd_and_even(1357902468) == (25, 20)
