from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(current: List[int], current_sum: int, start: int):
            if current_sum == target:
                answer.append(current.copy())
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                current_sum += candidates[i]
                if current_sum <= target:
                    backtrack(current, current_sum, i)
                current.pop()
                current_sum -= candidates[i]
        
        backtrack([], 0, 0)
        return answer