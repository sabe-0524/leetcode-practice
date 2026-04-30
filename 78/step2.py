from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        answer.append([])
        def backtrack(current: List[int], start: int):
            for i in range(start, len(nums)):
                current.append(nums[i])
                answer.append(current.copy())
                backtrack(current, i + 1)
                current.pop()
        
        backtrack([], 0)
        return answer