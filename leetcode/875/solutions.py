import math


class Solution:
    @staticmethod
    def consumption_time(piles: list[int], eating_rate: int):
        cons_time = 0
        for pile in piles:
            cons_time += math.ceil(pile / eating_rate)
        return cons_time

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        mini = 1
        maxi = max(piles)
        time_ = h
        eat_rate = float("inf")

        while mini <= maxi:
            mid = (mini + maxi) // 2
            cons_time = Solution.consumption_time(piles, mid)
            if cons_time <= h:
                if mid < eat_rate:
                    eat_rate = mid
                maxi = mid - 1
            else:
                mini = mid + 1
        return eat_rate


# PLEASE DO NOT CHANGE ANYTHING BELOW:
# TESTING ARENA:
sol = Solution()
# Test 1
p = [3, 6, 7, 11]
h = 8
e = 4
assert sol.minEatingSpeed(p, h) == e, "Failed!"

# Test 2
p = [25, 10, 23, 4]
h = 4
e = 25
assert sol.minEatingSpeed(p, h) == e, "Failed!"

# Test 3
p = [30, 11, 23, 4, 20]
h = 5
e = 30
assert sol.minEatingSpeed(p, h) == e, "Failed!"

# Test 4
p = [30, 11, 23, 4, 20]
h = 6
e = 23
assert sol.minEatingSpeed(p, h) == e, "Failed!"
