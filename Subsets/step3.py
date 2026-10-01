from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        
        def backtrack(current, idx):
            if idx >= len(nums):
                return
            current.append(nums[idx])
            answer.append(current.copy())
            backtrack(current, idx + 1)
            current.pop()
            backtrack(current, idx + 1)
        
        backtrack([], 0)
        return answer