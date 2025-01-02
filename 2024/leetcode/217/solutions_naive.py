def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    
    What is the Time Complexity of your solution?
    
    What is the Space Complexity of your solution?
    
    Can the time or space complexity be improved?
    
    What would you need to change in your previous answer to get there?
    """
    # =================== START HERE ===================
    for index, item in enumerate(nums):
        for j in range(index+1, len(nums)):
            if nums[j] == item:
                return True
    return False


assert contains_duplicate([1, 2, 3, 4]) is False
assert contains_duplicate([1, 2, 4, 4]) is True
