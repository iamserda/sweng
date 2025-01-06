"""Challenge:
Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.

Examples
calculate_exponent(4, 1024) ➞ 5

calculate_exponent(2, 1024) ➞ 10

calculate_exponent(9, 3486784401) ➞ 10
Notes
a is raised to the power of what in order to equal b?

source: edabit.com
"""


def calculate_exponent(base_num, total_num):
    """Given a base number, and a total sum, returns the exponent to which one can raise base number to get total. Therefore total is base to the power of exponent."""
    if total_num < base_num:
        return 0
    elif total_num == base_num:
        return 1
    else:
        new_total = total_num / base_num
        return 1 + calculate_exponent(base_num, total_num=new_total)


# Testing Arena:
assert calculate_exponent(4, 1024) == 5
assert calculate_exponent(2, 1024) == 10
assert calculate_exponent(9, 3486784401) == 10
