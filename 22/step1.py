from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(current: str, level: int):
            if len(current) == 2 * n:
                if level == 0:
                    answer.append(current)
                return
            if level < n:
                backtrack(current + "(", level + 1)
            if 0 < level:
                backtrack(current + ")", level - 1)
        
        backtrack("", 0)
        return answer