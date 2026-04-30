from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def recur_permute(current: List[int]):
            if len(current) == len(nums):
                answer.append(current.copy())
                return None
            for num in nums:
                if num in current:
                    continue
                current.append(num)
                recur_permute(current)
                current.pop()
        recur_permute([])
        return answer
                

