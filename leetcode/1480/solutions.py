class Solution:
    def running_sum(self, nums: list[int]) -> list[int]:
        arr = []
        for elem in nums:
            if not arr:
                arr.append(elem)
            else:
                arr.append(elem + arr[-1])
        return arr


# Testing Arena:
sol = Solution()
assert sol.running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
assert sol.running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
assert sol.running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
