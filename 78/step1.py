from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        answer.append([])
        def backtrack(current: List[int], start: int):
            if len(current) == len(nums):
                return
            for i, num in enumerate(nums):
                if i < start:
                    continue
                if num in current:
                    continue
                current.append(num)
                answer.append(current.copy())
                backtrack(current, i + 1)
                current.pop()
        
        backtrack([], 0)
        return answer