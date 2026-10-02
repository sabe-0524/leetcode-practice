from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        
        def backtrack(start, current_sum):
            if current_sum == target:
                result.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if current_sum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i])
                path.pop()
        
        backtrack(0, 0)
        return result