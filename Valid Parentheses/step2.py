from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairs = {
          "(" : ")",
          "{" : "}",
          "[" : "]"
        }
        
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if pairs[bracket] != ch:
                    return False
        
        return not stack                