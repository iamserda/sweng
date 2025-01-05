class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Write solution here:"""


sol = Solution()
assert sol.isPalindrome(12345) is not True
assert sol.isPalindrome(12321) is True
assert sol.isPalindrome(-12321) is not True
