from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def rob_line(arr: List[int]):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
            return dp[-1]
        
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))