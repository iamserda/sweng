# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quick_sorter(pairs, 0, len(pairs))
        return pairs

    def quick_sorter(self, arr: list, start: int, end: int) -> None:
        if end - start + 1 <= 1:
            return
        pivot = end - 1
        _next = start

        for index in range(start, pivot):
            if arr[index].key < arr[pivot].key:
                arr[_next], arr[index] = arr[index], arr[_next]
                _next += 1
        arr[pivot], arr[_next] = arr[_next], arr[pivot]
        self.quick_sorter(arr, start, _next)
        self.quick_sorter(arr, _next + 1, end)

    def converter(self, arr: list):
        return [(elem.key, elem.value) for elem in arr]


# TESTING ARENA:
pairs = [Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")]
sol = Solution()
print("pre:", sol.converter(pairs))
sol.quickSort(pairs)
print("post:", sol.converter(pairs))

pairs = [
    Pair(5, "apple"),
    Pair(9, "banana"),
    Pair(9, "cherry"),
    Pair(1, "date"),
    Pair(9, "elderberry"),
]
print("pre:", sol.converter(pairs))
sol.quickSort(pairs)
print("post:", sol.converter(pairs))
