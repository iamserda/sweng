"""
Given some integer x, print each digit within the integer.
constraint: you cannot convert the integer to any other data types.
"""
import random


def digit_in_number(num: int) -> int:
    """Prints each digit within the given integer 'num' arg."""


# TESTS ARENA:
# DO NOT MAKE ANY CHANGE TO THE CODE BELOW...

result = digit_in_number(10000)
print(result)

result = digit_in_number("10000")
print(result)

result = digit_in_number(random.randrange(10**6, 10**7-1))
print(result)

result = digit_in_number((1, 2, 3, 4, 5))
print(result)
