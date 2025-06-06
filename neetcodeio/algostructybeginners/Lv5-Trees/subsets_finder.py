# SCRATCH SOLUTION 3
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        arr = []
        if nums is None:
            return arr

        arr.append([])
        if len(nums) == 1:
            arr.append(nums)
        else:
            for i in range(len(nums)):
                arr.append([nums[i]])
                for j in range(i + 1, len(nums)):
                    arr.append([nums[i], nums[j]])
            arr.append(nums)
        print(arr)
        return arr


sol = Solution()
ans = sol.subsets([i for i in range(4)])
test = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

result = True
for a in ans:
    result = result and a in test
    if not result:
        print("Failed")
        break

# test2
ans = sol.subsets([1])
test = [[], [1]]

result = True
for a in ans:
    result = result and a in test
    if not result:
        print("Failed")
        break
