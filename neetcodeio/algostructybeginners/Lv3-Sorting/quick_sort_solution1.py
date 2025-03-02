import random


class Solution:

    def quickSort(self, arr):
        start, end = 0, len(arr)
        return self.quick_sorter(arr, start, end)

    def quick_sorter(self, arr, start, end):
        if end - start + 1 <= 1:
            return
        pivot_index = end - 1
        next_index = start
        for index in range(start, pivot_index):
            if arr[index] < arr[pivot_index]:
                arr[index], arr[next_index] = arr[next_index], arr[index]
                next_index += 1
        arr[next_index], arr[pivot_index] = arr[pivot_index], arr[next_index]
        self.quick_sorter(arr, start, next_index)
        self.quick_sorter(arr, next_index + 1, end)
        return arr


sol = Solution()
arr = [random.randrange(1, 100) for i in range(5)]
sorted_arr = sorted(arr)
sol.quickSort(arr)
assert arr == sorted_arr
