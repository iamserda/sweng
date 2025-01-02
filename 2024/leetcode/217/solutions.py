def contains_duplicates(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    
    What is the Time Complexity of your solution?
    O(n), please read the readme.md file for more info.
    
    What is the Space Complexity of your solution?
    O(n), please read the readme.md file for more info.
    
    Can the time or space complexity be improved?
    
    What would you need to change in your previous answer to get there?
    """
    # =================== START HERE ===================
    if not nums:
        return None
    return False if len(set(nums)) == len(nums) else True


assert contains_duplicates([1, 2, 3, 4]) is False
assert contains_duplicates([1, 2, 4, 4]) is True
assert contains_duplicates([]) is None
assert contains_duplicates(["1", 1, True, True]) is True
