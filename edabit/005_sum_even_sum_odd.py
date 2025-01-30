"""
CHALLENGE: Sum of Odd and Even Numbers
LINK: https://edabit.com/challenge/5XXXppAdfcGaootD9

Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list. The second element should be the sum of all odd numbers in the list.
Example

sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9] because  2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
sum_odd_and_even([0, 0]) ➞ [0, 0])

Notes: Count 0 as an even number.

"""

def sum_odd_and_even(arr: list):
    """Given a List of 0 or more values, return a List containing the sum of evven numers, and sum of odds numbers from the list received."""
    sum_odd = 0
    sum_even = 0

    if not arr:
        return [sum_even, sum_odd]

    for item in arr:
        if item % 2 == 0:
            sum_even += item
        else:
            sum_odd += item
    return [sum_even, sum_odd]


assert sum_odd_and_even([1, 2, 3, 4, 5, 6]) == [12, 9]
assert sum_odd_and_even([-1, -2, -3, -4, -5, -6]) == [-12, -9]
assert sum_odd_and_even([0, 0]) == [0, 0]
