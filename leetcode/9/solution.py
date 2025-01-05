class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x_ = x
        arr = []
        while x_ > 0:
            arr.append(x_ % 10)
            x_ //= 10
        start = 0
        end = len(arr) - 1

        while start <= end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True


sol = Solution()
assert sol.isPalindrome(12345) is not True
assert sol.isPalindrome(12321) is True
assert sol.isPalindrome(-12321) is not True
