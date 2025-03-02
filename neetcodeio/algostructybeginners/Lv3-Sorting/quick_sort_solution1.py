# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def quick_merge(arr1, arr2):
        
    def quickSort(self, pairs: list[Pair]) -> list[Pair]:
        if len(pairs) == 1:
            return pairs
        else:
            pivot = len(pairs) - 1
            nxt = 0
            for i in range(len(pairs) - 2):
                if pairs[i] <= pairs[pivot]:
                    pairs[i], pairs[nxt] = pairs[nxt], pairs[i]
                    nxt += 1
            pairs[pivot], pairs[nxt] = pairs[nxt], pairs[pivot]
            first_half = self.quickSort(pairs[: nxt + 1])
            second_half = self.quickSort(pairs[nxt + 1 :])
