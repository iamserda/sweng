from typing import List


# Challenge 1
def challenge1():
    """
    Challenge
    Implement the following functions:
    append_elements(arr1: List[int], arr2: List[int]) -> List[int].
    It should append the elements of arr2 to the end of arr1 and return the resulting list.

    pop_n(arr: List[int], n: int) -> List[int].
    It should remove the last n elements from the list and return the resulting list.
    If n is greater than the length of the list, it should return an empty list.

    insert_at(arr: List[int], index: int, element: int) -> List[int].
    It should insert the element at the specified index in the list and
    return the resulting list. If the index is out of bounds, you should
    insert it at the end of the list.
    """

    def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
        for item in arr2:
            arr1.append(item)
        return arr1

    def pop_n(arr: List[int], n: int) -> List[int]:
        if len(arr) < n:
            return []

        for i in range(n):
            arr.pop()
        return arr

    def insert_at(arr: List[int], index: int, element: int) -> List[int]:
        if index > len(arr):
            arr.append(element)
        else:
            arr.insert(index, element)
        return arr

    # do not modify below this line
    print(append_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
    print(append_elements([4, 3], [4, 5, 3]))  # [4, 3, 4, 5, 3]
    print(pop_n([1, 2, 3, 4, 5], 2))  # [1, 2, 3]
    print(pop_n([1, 2, 3, 4, 5], 6))  # []
    print(pop_n([1, 2, 3, 4, 5], 5))  # []
    print(insert_at([1, 2, 3, 4, 5], 2, 6))  # [1, 2, 6, 3, 4, 5]
    print(insert_at([1, 2, 3, 4], 6, 5))  # [1, 2, 3, 4, 5]


# Challenge 2
def challenge2():
    """pass"""
    def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
        for item in arr2:
            arr1.append(item)
        return arr1

    def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
        for item in arr2:
            if item in arr1:
                arr1.remove(item)
        return arr1

    # do not modify below this line
    print(append_elements([1, 2, 3], [4, 5, 6]))
    print(append_elements([4, 3], [4, 5, 3]))

    print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
    print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
    print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))


# Challenge 3
def challenge3():
    """pass"""

    def combine_elements(arr1: List[int], arr2: List[int]) -> List[int]:
        return arr1 + arr2

    # do not modify below this line
    arr1 = [1, 3, 5]
    arr2 = [4, 6, 8]

    print(combine_elements(arr1, arr2))  # [1, 3, 5, 4, 6, 8]
    print(arr1)  # [1, 3, 5]
    print(arr2)  # [4, 6, 8]


# Challenge 4
def challenge4():
    """pass"""
    def create_list_with_value(size: int, index: int, value: int) -> List[int]:
        return [0 if i != index else value for i in range(size)]

    # do not modify below this line
    print(create_list_with_value(5, 3, 7))  # [0, 0, 0, 7, 0]
    print(create_list_with_value(1, 0, 5))  # [5]
    print(create_list_with_value(10, 9, 9))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 9]
    print(create_list_with_value(10, 9, 0))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Challenge 5
def challenge5():
    """pass"""
    def remove_element(arr: List[int], element: int) -> List[int]:
        return [i for i in arr if i != element]

    # do not modify below this line
    arr = [1, 3, 5, 7, 9]

    print(remove_element(arr, 3))
    # [1, 5, 7, 9]

    print(arr)
    # [1, 3, 5, 7, 9]

    print(remove_element(arr, 9))
    # [1, 3, 5, 7]

    print(arr)
    # [1, 3, 5, 7, 9]

    print(remove_element(arr, 1))
    # [3, 5, 7, 9]

    print(arr)
    # [1, 3, 5, 7, 9]



# Challenge 6
def challenge6():
    """pass"""

    def create_list_of_odds(n: int) -> List[int]:
        return [i for i in range(1, n+1, 2)]


    # do not modify below this line
    print(create_list_of_odds(1))
    # [1]

    print(create_list_of_odds(5))
    # [1, 3, 5]

    print(create_list_of_odds(6))
    # [1, 3, 5]

    print(create_list_of_odds(10))
    # [1, 3, 5, 7, 9]


# TESTING GROUND
print("\nChallenge 1: ")
challenge1()
print("\nChallenge 2: ")
challenge2()
print("\nChallenge 3: ")
challenge3()
print("\nChallenge 4: ")
challenge4()
print("\nChallenge 5: ")
challenge5()
print("\nChallenge 6: ")
challenge6()
