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
    print(append_elements([1, 2, 3], [4, 5, 6])) # [1, 2, 3, 4, 5, 6]
    print(append_elements([4, 3], [4, 5, 3])) # [4, 3, 4, 5, 3]
    print(pop_n([1, 2, 3, 4, 5], 2)) # [1, 2, 3]
    print(pop_n([1, 2, 3, 4, 5], 6))# []
    print(pop_n([1, 2, 3, 4, 5], 5)) # []
    print(insert_at([1, 2, 3, 4, 5], 2, 6)) # [1, 2, 6, 3, 4, 5]
    print(insert_at([1, 2, 3, 4], 6, 5)) # [1, 2, 3, 4, 5]


# Challenge 2

# Challenge 3

# Challenge 4

# Challenge 5

# Challenge 6

# Challenge 7

# Challenge 8


# TESTING GROUND
challenge1()
# challenge2()
# challenge3()
# challenge4()
# challenge5()
# challenge6()
# challenge7()
# challenge8()