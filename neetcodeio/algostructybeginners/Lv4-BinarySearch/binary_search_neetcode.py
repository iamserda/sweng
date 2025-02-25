class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums:
            left_index = 0
            right_index = len(nums) - 1
            while left_index <= right_index:
                mid = (left_index + right_index) // 2
                if target > nums[mid]:
                    left_index = mid + 1
                elif target < nums[mid]:
                    right_index = mid - 1
                else:
                    return mid
        return -1


# walktrhough:
nums = [10, 15, 20, 25, 30, 35]
# index= [0, 1, 2, 3, 4, 5 ]
target = 35
sol = Solution()
assert sol.search(nums, target) != -1

# left = 0
# right = 6 - 1 = 5

# while left <= right => 0 <= 5 => True:
# mid = (0 + 5) // 2 = 2
# is nums[2] > target => 20 > 35 => False
# is nums[2] < target => 20 < 35 => True: left = mid + 1, left = 3

# while left <= right => 3 <= 5 => True:
# mid = (3 + 5) // 2 = 4
# is nums[4] > target => 30 > 35 => False
# is nums[4] < target => 30 < 35 => True: left = mid + 1, left = 5

# while left <= right => 5 <= 5 => True:
# mid = (5 + 5) // 2 = 5
# is nums[5] > target => 35 > 35 => False
# is nums[5] < target => 35 < 35 => False
# then return mid

nums = [10, 15, 20, 25, 30, 35]
# index= [0, 1, 2, 3, 4, 5 ]
target = 11
sol = Solution()
assert sol.search(nums, target) == -1
