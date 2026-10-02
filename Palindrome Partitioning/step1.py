from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(t: str):
            left = 0
            right = len(t) - 1
            while left < right:
                if t[left] != t[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        result = []
        path = []
        def backtrack(start):
            if start == len(s):
                result.append(path.copy())
                return
            
            for i in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:i]):
                    path.append(s[start:i])
                    backtrack(i)
                    path.pop()
        
        backtrack(0)
        return result
