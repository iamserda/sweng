"""
CHALLENGE: Maximum Edge of a Triangle at https://edabit.com/challenge/Zerwo2AENbvRZTe83
formula, side1 + side2 - 1 = maximum edge
"""


def next_edge(side1=1, side2=1):
    """calculates the length of the third side of a triangle C, given 2 sides A and B."""
    return side1 + side2 - 1


assert next_edge(8, 10) == 17
assert next_edge(5, 7) == 11
assert next_edge(9, 2) == 10
