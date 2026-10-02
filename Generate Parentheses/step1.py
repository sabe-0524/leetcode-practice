from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        
        def backtrack(left, right):
            if left < right or left > n:
                return
            if right == n:
                result.append("".join(path))
                return
            
            path.append("(")
            backtrack(left + 1, right)
            path.pop()
            
            path.append(")")
            backtrack(left, right + 1)
            path.pop()
        
        backtrack(0, 0)
        return result