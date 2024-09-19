"""Section 4: Stacks and Queues"""

from typing import List, Deque
from collections import deque


# Challenge 1:
def challenge1():
    """pass"""

    def reverse_list(arr: List[int]) -> List[int]:
        new_arr = []
        while len(arr):
            new_arr.append(arr.pop())
        return new_arr

    # do not modify below this line
    print(reverse_list([1, 2, 3]))
    print(reverse_list([3, 2, 1, 4, 6, 2]))
    print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

