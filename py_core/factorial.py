def factorial(n: int) -> int:
    """
    Compute n! (factorial) for a non-negative integer n.

    Args:
        n: Non-negative integer whose factorial to compute.

    Returns:
        The factorial of n.

    Raises:
        TypeError: If n is not an int.
        ValueError: If n is negative.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"Value entered {n} must be an integer.")
    if n < 0:
        raise ValueError(f"Value {n} cannot be a non-negative integer.")
    if n == 0:
        return 1
    total = 1
    for i in range(1, int(n) + 1):
        total *= i
    return total


# Testing Arena:
test_num = -1
try:
    factorial(test_num)
except ValueError as err:
    print(f"ValueError Occurred: {err}")

test_num = "A"
try:
    factorial(test_num)
except TypeError as err:
    print(f"TypeError Occurred: {err}")

test_num = 0
assert factorial(test_num) == 1

test_num = 1
assert factorial(test_num) == 1

test_num = 5
assert factorial(test_num) == 120

# Efficiency Talkspace:
# - Time: O(n) because the number of operations will be linear/proportional to the size of input 'n'.
# - Space: O(1) because total is used as an accumulator where I overwrite the previously stored value.
