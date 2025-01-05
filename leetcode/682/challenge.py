"""calculate_points solution for leetcode problem 685."""

def calculate_points(operations: list[str]) -> int:
    """Given an array as input, apply the operations, 
    and return the sum of your results. See readme.md for more info. """
    

assert calculate_points(["5","2","C","D","+"]) == 30
assert calculate_points(["5","-2","4","C","D","9","+","+"]) == 27
assert calculate_points(["1","C"]) == 0
