# SCRATCH SOLUTION 2
import math


class Solution:
    @staticmethod
    def consumption_time(piles, eating_rate):
        cons_time = 0
        for pile in piles:
            cons_time += math.ceil(pile / eating_rate)
        return cons_time

    def min_eating_speed(self, piles: list[int], h: int) -> int:
        mini = 1
        maxi = sum(piles)
        time_ = h
        eat_rate = float("inf")

        while mini <= maxi:
            mid = (mini + maxi) // 2
            print(mini, maxi, mid)
            cons_time = Solution.consumption_time(piles, mid)
            if cons_time <= h:
                if mid < eat_rate:
                    eat_rate = mid
                maxi = mid - 1
            else:
                mini = mid + 1
        print(eat_rate)
        return eat_rate


sol = Solution()
assert sol.min_eating_speed(piles=[1, 4, 3, 2], h=9) == 2
assert sol.min_eating_speed(piles=[25, 10, 23, 4], h=4) == 25
