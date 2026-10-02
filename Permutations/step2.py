from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i, num in enumerate(nums):
                if used[i] == True:
                    continue
                
                path.append(num)
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        
        backtrack()
        return result