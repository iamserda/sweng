from random import randint

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


# PLEASE DO NOT EDIT ANY CODE WITHIN THIS FUNCTION
def guess(num: int):
    if isinstance(num, int):
        if num > Solution.guessed_num:
            return -1
        if num < Solution.guessed_num:
            return 1
        else:
            return 0


class Solution:
    guessed_num = 0

    # Start here, do not change any code above:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                end = mid - 1
            elif result == 1:
                start = mid + 1


# PLEASE DO NO EDIT ANY CODE BELOW HERE
# TESTING ARENA:
if __name__ == "__main__":
    # Do not change test-data below:
    n = 10
    Solution.guessed_num = 6
    sol = Solution()
    assert Solution.guessed_num == sol.guessNumber(n)

    n = 1
    Solution.guessed_num = 1
    sol = Solution()
    assert Solution.guessed_num == sol.guessNumber(n)

    n = 2
    Solution.guessed_num = 1
    sol = Solution()
    assert Solution.guessed_num == sol.guessNumber(n)
