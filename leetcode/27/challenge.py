def remove_element(nums: list[int], val: int) -> int:
    """
    Given an integer array nums and an integer val,
    remove all occurrences of val in nums in-place.
    The order of the elements may be changed.
    Then return the number of elements in nums which are not equal to val.
    """
    [1, 2, 3, 3, 4, 4, 7]
    left = 0
    right = len(nums) - 1
    nums.sort()
    print(nums)
    if nums[left] > val:
        return len(nums)

    while left < right:
        if nums[left] == val:
            if nums[right] == val:
                right = left
                break
            else:
                nums[left] = nums[right]
                left += 1
                right -= 1
                continue
        left += 1
    print(nums)
    return right

# TESTING ARENA
arr = [3, 2, 2, 3]
assert remove_element(arr, 3) == 2
arr = [0, 1, 2, 2, 3, 0, 4, 2]
assert remove_element(arr, 2) == 5
arr = [1]
assert remove_element(arr, 1) == 0
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert remove_element(arr, 1) == 0
arr = [2]
assert remove_element(arr, 3) == 