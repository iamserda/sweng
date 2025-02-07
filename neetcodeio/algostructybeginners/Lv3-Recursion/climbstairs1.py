def climbStairs(n: int) -> int:
    def climb(count, n):
        if count > n:
            return 0
        if count == n:
            return 1
        else:
            return climb(count + 1, n) + climb(count + 2, n)

    if n == 0:
        return 0
    if n == 1:
        return 1
    result = climb(0, n)
    print(result)
    return result


assert climbStairs(5) == 8
# assert climbStairs(30) == 8  # memoization is needed here.
