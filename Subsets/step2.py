from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        for mask in range(1 << n):
            current = []
            
            for i in range(n):
                if mask & (1 << i):
                    current.append(nums[i])
            
            answer.append(current)
        
        return answer