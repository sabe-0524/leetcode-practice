from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = defaultdict(int)
        longest = 0
        for num in nums:
            if sequence[num]:
                continue
            length_prev = sequence[num - 1]
            length_next = sequence[num + 1]
            length = length_prev + length_next + 1
            sequence[num - length_prev] = length
            sequence[num + length_next] = length
            sequence[num] = length
            longest = max(length, longest)
        
        return longest