# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# Start here:
class Solution:
    first_bad_bad = 0

    def firstBadVersion(self, n: int) -> int:
        pass


# PLEASE DO NOT CHANGE ANYTHING BELOW:
# TESTING ARENA:
if __name__ == "__main__":
    Solution.first_bad_bad = 4
    sol = Solution()
    assert sol.firstBadVersion(n=5) == 4

    Solution.first_bad_bad = 1
    sol = Solution()
    assert sol.firstBadVersion(n=1) == 1
