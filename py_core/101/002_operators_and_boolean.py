# this is a single-line comment
"""this is
a multiline comment.
also known as docstring as in documentation strings"""

# addition
print(1 + 1)

# subtraction
print(2 * 41)

# multiplication
print(1 - 1)

# division
print(10 / 5)

# strictly-integer division
print(10 // 5)

# modulo arithmetic division
print(10 % 5)

# boolean: True, False
a = True
b = False
print("\n", a)
print(b)
# 0 is the False(y) value for numbers
print("\nbool(0):", bool(0))  # False
# any number other than 0 is True
print("bool(1):", bool(b))  # True
print("bool(-1)", bool(-1))  # True

# logical operator: and
print("\nTrue and True is:", True and True)  # True
print("True and False is:", True and False)  # False
print("False and False is:", False and False)  # False
print("False and True is:", False and True)  # False

# logical operator: or
print("\nTrue or True is:", True or True)  # True
print("False or True is:", False or True)  # True
print("True or False is:", True or False)  # True
print("False or False is:", False or False)  # False

# equality, less-than, greater-than,
# less-than-or-equal, greater-than-or-equal

# equality operator ==
print()
print(1 == 1)  # True
print(10 == 20)  # False

# less-than <
print("7 < 5:", 7 < 5)  # False
print("7 < 15:", 7 < 15)  # True

# less-than or equal <=
print("7 <= 5:", 7 <= 5)  # False
print("5 <= 5:", 5 <= 5)  # True

# greater-than >
print("7 > 5:", 7 <= 5)  # True
print("7 > 15:", 7 <= 15)  # False

# greater-than or equal
print("1 >= 1", 1 >= 1)  # True
print("1 >= 10", 1 >= 10)  # False
