from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        answer = 0
        sum_dict = defaultdict(int)
        for num in nums:
            cumulative_sum += num
            if cumulative_sum == k:
                answer += 1
            if cumulative_sum - k in sum_dict:
                answer += sum_dict[cumulative_sum - k]
            sum_dict[cumulative_sum] += 1
        return answer