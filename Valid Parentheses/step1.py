from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                q.append(ch)
            else:
                if not q:
                    return False
                bracket = q.pop()
                if (bracket == "(" and ch != ")") or (bracket == "{" and ch != "}") or (bracket == "[" and ch != "]"):
                    return False
        
        return True if not q else False