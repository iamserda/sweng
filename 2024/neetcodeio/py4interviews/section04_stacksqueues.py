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


# Challenge 2:
def challenge2():
    """pass"""

    def rotate_list(arr: List[int], k: int) -> Deque[int]:
        my_queue = deque(arr)
        for i in range(k):
            my_queue.append(my_queue.popleft())
        return my_queue

    # do not modify below this line
    print(rotate_list([1, 2, 3, 4, 5], 0))
    print(rotate_list([1, 2, 3, 4, 5], 1))
    print(rotate_list([1, 2, 3, 4, 5], 2))
    print(rotate_list([1, 2, 3, 4, 5], 3))
    print(rotate_list([1, 2, 3, 4, 5], 4))
    print(rotate_list([1, 2, 3, 4, 5], 5))

    # Expected Output:
    # deque([1, 2, 3, 4, 5])
    # deque([2, 3, 4, 5, 1])
    # deque([3, 4, 5, 1, 2])
    # deque([4, 5, 1, 2, 3])
    # deque([5, 1, 2, 3, 4])
    # deque([1, 2, 3, 4, 5])


# Challenge 3:
def challenge3():
    """pass"""

    def rotate_list(arr: List[int], k: int) -> Deque[int]:
        my_queue = deque(arr)
        for _ in range(k):
            my_queue.appendleft(my_queue.pop())
        return my_queue

    # do not modify below this line
    print(rotate_list([1, 2, 3, 4, 5], 0))  # deque([1, 2, 3, 4, 5])
    print(rotate_list([1, 2, 3, 4, 5], 1))  # deque([5, 1, 2, 3, 4])
    print(rotate_list([1, 2, 3, 4, 5], 2))  # deque([4, 5, 1, 2, 3])
    print(rotate_list([1, 2, 3, 4, 5], 3))  # deque([3, 4, 5, 1, 2])
    print(rotate_list([1, 2, 3, 4, 5], 4))  # deque([2, 3, 4, 5, 1])
    print(rotate_list([1, 2, 3, 4, 5], 5))  # deque([1, 2, 3, 4, 5])


print("\nChallenge 1:")
challenge1()
print("\nChallenge 2:")
challenge2()
print("\nChallenge 3:")
challenge3()
