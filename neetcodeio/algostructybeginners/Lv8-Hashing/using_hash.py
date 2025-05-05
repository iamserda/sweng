class Solution:
    def name_counter(self, names):
        # a hashtable/dictionary to keep tabs on how many times I have seen this name.
        dictio = {}
        for name in names:
            if not dictio.get(name):
                dictio[name] = 1
            else:
                dictio[name] += 1
        return dictio


# Testing:
sol = Solution()
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]
expected = {"alice": 1, "brad": 2, "collin": 1, "dylan": 1, "kim": 1}
actual = sol.name_counter(names)
assert actual == expected
