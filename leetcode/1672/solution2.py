class Solution:
    def maximumWealth(self, accounts: list) -> int:
        if not accounts:
            return
        wealthiest = float("-inf")
        for account in accounts:
            wealthiest = max(wealthiest, sum(account))
        return wealthiest


sol = Solution()
assert sol.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
assert sol.maximumWealth([[1, 2, 3], [4, 5, 7], [1, 3, 9]]) == 16
assert sol.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
