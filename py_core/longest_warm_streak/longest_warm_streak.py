def longest_warm_streak(temps, threshold):
    if not temps:
        return 0
    maxi = float("-inf")
    start = -1
    for end in range(len(temps)):
        if temps[end] > threshold:
            if start == -1:
                start = end
                maxi = max(1, maxi)
            else:
                new_streak = (end - start) + 1
                maxi = max(new_streak, maxi)
        else:
            start = -1
    return maxi


tps = [1, 2, 3, 3, 1, 4, 6, 7, 4, 0, 11, 12, 1]
ths = 1
assert longest_warm_streak(tps, ths) == 4

tps = [1, 2, 3, 3, 4, 4, 6, 7, 4, 1, 11, 12, 3]
ths = 2
assert longest_warm_streak(tps, ths) == 7
