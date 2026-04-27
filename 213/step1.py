from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len (nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        l_dp = dp[-2]
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums) - 3, 0, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        r_dp = dp[1]
        return max(l_dp, r_dp)