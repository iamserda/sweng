class Solution:
    def binary_search(self, arr, target):
        if arr:
            L = 0
            R = len(arr) - 1
            while L <= R:
                mid = (L + R) // 2
                if target > arr[mid]:
                    L = mid + 1
                elif target < arr[mid]:
                    R = mid - 1
                else:
                    return True
        return False

    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        """Time: O(m * logn)"""
        if matrix:
            for arr in matrix:  # O(n where n is len(matrix))
                if target < arr[0] or target > arr[-1]:
                    continue
                result = self.binary_search(
                    arr, target
                )  # O(log m, where m is len(arr))
                if result:
                    return True
        return False


# TESTING ARENA:
sol = Solution()

matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10
assert sol.search_matrix(matrix, target) == True

matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 15
assert sol.search_matrix(matrix, target) == False
