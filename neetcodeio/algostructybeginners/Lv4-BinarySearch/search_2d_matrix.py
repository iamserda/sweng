class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        pass


# TESTING ARENA:
sol = Solution()

matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10
assert sol.search_matrix(matrix, target) == True

matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 15
assert sol.search_matrix(matrix, target) == False
