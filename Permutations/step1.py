from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        remain = nums.copy()
        
        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for candidate in remain.copy():
                path.append(candidate)
                remain.remove(candidate)
                backtrack()
                path.pop()
                remain.append(candidate)
        
        backtrack()
        return result