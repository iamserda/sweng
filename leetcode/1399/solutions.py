class Solution:
    def countLargestGroup(self, n: int) -> int:
        dictio = {}
        maxi = 1
        for i in range(1, n + 1):
            if i <= 9:
                dictio[i] = [i]
            else:
                num = 0
                temp = i
                while temp > 0:
                    num += temp % 10
                    temp = temp // 10
                if num in dictio:
                    dictio[num].append(i)
                else:
                    dictio[num] = [i]
                maxi = max(maxi, len(dictio[num]))
        print(maxi)
        count = 0
        for value in dictio.values():
            print(value)
            if len(value) == maxi:
                count += 1

        return count


sol = Solution()
assert sol.countLargestGroup(13) == 4
assert sol.countLargestGroup(2) == 2
assert sol.countLargestGroup(173) == 1
