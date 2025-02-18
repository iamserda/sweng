class Solution:

    def selection_sort(self, arr: list) -> list:
        for i in range(len(arr)):
            # where to place the next smallest value
            min_index = i

            for j in range(i, len(arr)):
                # find the index of the smallest value
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                # swap the value at i with the value at min_index
                arr[i], arr[min_index] = arr[min_index], arr[i]


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
