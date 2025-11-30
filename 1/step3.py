from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [values[diff], i]
            else:
                values[num] = i
        return []