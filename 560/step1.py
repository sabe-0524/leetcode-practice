from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            num = 0
            for j in range(i, len(nums)):
                num += nums[j]
                if num == k:
                    answer += 1
        return answer
