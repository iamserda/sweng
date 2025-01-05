def contains_duplicates(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    
    What is the Time Complexity of your solution?
    
    What is the Space Complexity of your solution?
    
    Can the time or space complexity be improved?
    
    What would you need to change in your previous answer to get there?
    """
    # =================== START HERE ===================


# TESTS ARENA
assert contains_duplicates([1, 2, 3, 4]) is False
assert contains_duplicates([1, 2, 4, 4]) is True
assert contains_duplicates([]) is False
assert contains_duplicates(["1", 1, True, True]) is False
