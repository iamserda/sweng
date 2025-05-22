import random

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    first_bad_version = 0

    @staticmethod
    def isBadVersion(version: int):
        return version >= Solution.first_bad_version

    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        first_bad_version = n

        while start <= end:
            mid = (start + end) // 2
            if Solution.isBadVersion(mid):
                first_bad_version = (
                    mid if mid < first_bad_version else first_bad_version
                )
                end = mid - 1
            else:
                start = mid + 1
        return first_bad_version


# PLEASE DO NOT CHANGE ANYTHING BELOW:
# TESTING ARENA:
if __name__ == "__main__":
    Solution.first_bad_version = random.randint(1, 100)
    sol = Solution()
    assert sol.firstBadVersion(n=100) == Solution.first_bad_version

    Solution.first_bad_version = 4
    assert sol.firstBadVersion(n=5) == Solution.first_bad_version

    Solution.first_bad_bad = 1
    assert sol.firstBadVersion(n=1) == 1
