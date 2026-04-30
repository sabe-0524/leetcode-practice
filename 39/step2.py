from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(current: List[int], current_sum: int, start: int):
            if current_sum == target:
                answer.append(current.copy())
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if current_sum + num <= target:
                    current.append(num)
                    backtrack(current, current_sum + num, i)
                    current.pop()
        
        backtrack([], 0, 0)
        return answer