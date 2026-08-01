from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current = 1
        prev = None
        for num in nums:
            if prev is not None:
                if num - prev == 1:
                    current += 1
                    longest = max(longest, current)
                elif num - prev == 0:
                    pass
                else:
                    current = 1
            prev = num
        
        return longest