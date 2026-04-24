from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(len(nums)):
            if i == 0:
                continue
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
        return max(dp)