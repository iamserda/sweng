class Solution:

    def selection_sort(self, arr: list) -> list:
        pass


sol = Solution()
arr = [4, 3, 2, 1]
sol.selection_sort(arr)
assert arr == [1, 2, 3, 4]

arr = [10, 1, 20, 2, 30, 3, 4, 40, 5]
sol.selection_sort(arr)
assert arr == [1, 2, 3, 4, 5, 10, 20, 30, 40]

arr = [0, 4, 3, 2, 4, 0]
sol.selection_sort(arr)
assert arr == [0, 0, 2, 3, 4, 4]

arr = [1, 3, 5, 4, 2]
sol.selection_sort(arr)
assert arr == [1, 2, 3, 4, 5]
