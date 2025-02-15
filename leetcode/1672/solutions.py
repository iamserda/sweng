class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxi = float("-inf")
        for account in accounts:
            new_sum = self.accounts_sum(account)
            maxi = maxi if maxi > new_sum else new_sum
        return maxi

    def accounts_sum(self, accounts):
        _sum = 0
        for account_bal in accounts:
            _sum += account_bal
        return _sum


sol = Solution()
assert sol.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
assert sol.maximumWealth([[1, 2, 3], [4, 5, 7], [1, 3, 9]]) == 16
assert sol.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
