class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1 or s[0] in ")}]":
            return False

        pairs = set(["{}", "[]", "()"])
        store = []
        for index, value in enumerate(s):
            if store and store[-1] + value in pairs:
                store.pop()
            else:
                store.append(value)
        if not store:
            return True
        return False

sol = Solution()
isValid = sol.isValid
assert isValid("[") == False
assert isValid("()") == True
assert isValid("()[]{}") == True
assert isValid("(]") == False
assert isValid("([])") == True
