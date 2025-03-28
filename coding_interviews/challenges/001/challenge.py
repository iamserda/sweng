"""Challenge:
Given an array of integers, return the first pair of numbers where their product is some integer K. For example: K = num1 x num2.
Both num1 and num2 are in the array
Both num1 and num2 are not the same number.
[2,40,1,6,5,4,-1] -> K=20 => 5, 4 since 5 x 4 = 20
"""


def solution(arr: list[int], k: int) -> tuple:
    pass  # delete 'pass' and show me the code!


assert solution([3, 6, 2, 15, 9, 7, 5, 10], k=30) == (2, 15) or (15, 2)
assert solution([3, 2, 15, 9, 7, 5, 10], k=45) == (3, 15) or (15, 3) or (9, 5) or (5, 9)
