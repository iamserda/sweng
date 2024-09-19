from typing import List

def challenge1():
    """pass """
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
    """pass """
    

def challenge3():
    """pass """
    

