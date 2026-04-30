from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(current: str, left: int, right: int):
            if len(current) == 2 * n:
                answer.append(current)
                return
            if left > right:
                backtrack(current + ")", left, right + 1)
            if left < n:
                backtrack(current + "(", left + 1, right)
        
        backtrack("", 0, 0)
        return answer