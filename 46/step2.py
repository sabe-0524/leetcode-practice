from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        used = [False] * len(nums)
        def recur_permute(current: List[int]):
            if len(current) == len(nums):
                answer.append(current.copy())
                return
            for i, num in enumerate(nums):
                if used[i] == False:
                    used[i] = True
                    current.append(num)
                    recur_permute(current)
                    used[i] = False
                    current.pop()
        
        recur_permute([])
        return answer
                