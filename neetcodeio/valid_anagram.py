class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s and t and len(s) == len(t):
            dictio = {}
            for char in s:
                if char in dictio:
                    dictio[char] += 1
                else:
                    dictio[char] = 1
            for char in t:
                if char in dictio:
                    dictio[char] -= 1
                    if dictio[char] == 0:
                        del dictio[char]
                else:
                    dictio[char] = 1
            if not dictio:
                return True
        return False
