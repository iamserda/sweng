"""
one liner by Nick Proshin and blackburnfjames on Leetcode:
https://leetcode.com/problems/richest-customer-wealth/solutions/2675823/python-1-liner-simple-solution"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(acc) for acc in accounts)


sol = Solution()
assert sol.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
assert sol.maximumWealth([[1, 2, 3], [4, 5, 7], [1, 3, 9]]) == 16
assert sol.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
