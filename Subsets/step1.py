from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        length = len(nums)
        scope = 2 ** length
        for i in range(scope):
            current = []
            idx = 0
            while i > 0:
                if i & 1:
                    current.append(nums[idx])
                
                i = i >> 1
                idx += 1
            answer.append(current)
        
        return answer