from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        
        def backtrack(idx):
            if idx == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()
            backtrack(idx + 1)
        
        backtrack(0)
        return result
        