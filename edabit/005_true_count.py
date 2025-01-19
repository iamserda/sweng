"""
Source: Edabit.com
Title: How Much is True?
Author: Joshua Señoron
Description: "Create a function which returns the number of True values in a list."
Examples: ["count_true([True, False, False, True, False]) ➞ 2", "count_true([False, False, False, False]) ➞ 0","count_true([]) ➞ 0"]
Notes: ["Return 0 if given an empty list.", "All list items are of the type bool (True or False)."]
"""


def count_true(lst):
    return len([x for x in lst if x == True])
