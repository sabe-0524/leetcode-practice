from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1
        
        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - k]
            freq[prefix_sum] += 1
        
        return count