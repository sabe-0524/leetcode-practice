from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = len(nums) + 1
        start = 0
        min_len = INF
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                min_len = min(min_len, i - start + 1)
                current_sum -= nums[start]
                start += 1
        
        return min_len if min_len != INF else 0

