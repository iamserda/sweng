# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        for i in range(len(pairs)):
            j = i - 1
            curr_key = pairs[j].key
            nxt_key = pairs[j + 1].key
            while j >= 0 and curr_key > nxt_key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
                curr_key = pairs[j].key
                nxt_key = pairs[j + 1].key
            output.append([*pairs])
        return output

    def convert_to_2D_arr(self, arr):
        result_arr = []
        for row in arr:
            new_row = []
            for item in row:
                new_row.append((item.key, item.value))
            result_arr.append(new_row)
        return result_arr


pair1 = Pair(5, "apple")
pair2 = Pair(2, "banana")
pair3 = Pair(9, "cherry")

sol = Solution()
arr = [pair1, pair2, pair3]
final_answer = sol.convert_to_2D_arr(sol.insertionSort(arr))

expected_output = [
    [(5, "apple"), (2, "banana"), (9, "cherry")],
    [(2, "banana"), (5, "apple"), (9, "cherry")],
    [(2, "banana"), (5, "apple"), (9, "cherry")],
]

assert final_answer == expected_output
print(final_answer)
