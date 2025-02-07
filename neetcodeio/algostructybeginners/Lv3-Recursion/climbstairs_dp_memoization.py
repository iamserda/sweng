class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        mem = {}
        result = self.climb(0, n, mem)
        print(result, mem)
        return result

    def climb(self, count, n, mem):
        """Recursive routine where mem is a dict storing previous values"""
        if count in mem:
            return mem[count]
        if count > n:
            mem[count] = 0
            return 0
        if count == n:
            mem[count] = 1
            return 1
        else:
            if count + 1 not in mem:
                mem[count + 1] = self.climb(count + 1, n, mem)
            if count + 2 not in mem:
                mem[count + 2] = self.climb(count + 2, n, mem)
            return mem[count + 1] + mem[count + 2]


sol = Solution()
assert sol.climbStairs(5) == 8
assert sol.climbStairs(15) == 987
