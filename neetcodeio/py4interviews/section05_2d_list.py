from typing import List


def challenge1():
    """pass"""

    def find_max_in_each_list(nested_arr: List[int]) -> List[int]:
        maxes = []
        for row in nested_arr:
            maxes.append(max(row))
        return maxes

    # do not modify below this line
    print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
    print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))

    # EXPECTED OUTPUT:
    # [2, 4]
    # [3, 6, 9]
    # [8, 9, 10, 11]


def challenge2():
    """pass"""

    def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
        """pass"""
        try:
            item = grid[r][c]
            return True
        except IndexError as err:
            return False

    # do not modify below this line
    print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
    print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
    print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
    print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
    print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
    print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
    print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))

    # EXPECTED OUTPUT
    # True
    # True
    # True
    # False
    # False
    # False
    # False


def challenge3():
    """pass"""



if __name__ == "__main__":
    # TESTING GROUND:
    print("\nChallenge 1: ")
    challenge1()
    print("\nChallenge 2: ")
    challenge2()
    print("\nChallenge 3: ")
    challenge3()
