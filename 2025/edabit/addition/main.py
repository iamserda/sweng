def addition(num1: int = 0, num2: int = 0) -> int:
    """Receives two numbers, num1 and num2, return the sum of those two numbers.
    If nothing is received, it returns 0.
    """
    return num1 + num2


assert addition(3, 2) == 5
assert addition(-3, -6) == -9
assert addition(7, 3) == 10
