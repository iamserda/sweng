def remove_element(nums: list[int], val: int) -> int:
    """Given an integer array nums and an integer val, remove all occurrences of val in nums **in-place**. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val."""
    if not nums:
        return 0

    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        if nums[left_index] == val:
            if nums[left_index] == nums[right_index]:
                right_index -= 1
            else:
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
                left_index += 1
                right_index -= 1
            nums.pop()
            continue
        left_index += 1
    return len(nums)


arr = [3, 2, 2, 3]
assert remove_element(arr, 3) == 2
arr = [0, 1, 2, 2, 3, 0, 4, 2]
assert remove_element(arr, 2) == 5
arr = [1]
assert remove_element(arr, 1) == 0
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert remove_element(arr, 1) == 0
