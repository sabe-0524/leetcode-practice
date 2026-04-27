from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(2, len(nums)):
            dp[i] += max(dp[:(i - 1)])
        
        return max(dp)