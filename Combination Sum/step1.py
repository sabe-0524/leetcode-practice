from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        candidate = []
        
        def backtrack(idx, current_sum):
            if idx == len(nums) or current_sum > target:
                return
            
            if current_sum == target:
                result.append(candidate.copy())
                return
            
            candidate.append(nums[idx])
            current_sum += nums[idx]
            
            backtrack(idx, current_sum)
            
            candidate.pop()
            current_sum -= nums[idx]
            
            backtrack(idx + 1, current_sum)
        
        backtrack(0, 0)
        return result