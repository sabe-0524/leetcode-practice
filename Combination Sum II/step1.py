from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        
        def backtrack(idx, current_sum):
            if current_sum == target:
                if path not in result:
                    result.append(path.copy())
                return
            
            if idx == len(candidates) or current_sum > target:
                return
            
            path.append(candidates[idx])
            backtrack(idx + 1, current_sum + candidates[idx])

            path.pop()
            backtrack(idx + 1, current_sum)
        
        backtrack(0, 0)
        return result