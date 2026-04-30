class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        index = 0
        for ch in t:
            if ch == s[index]:
                index += 1
            if index == len(s):
                return True
        return False