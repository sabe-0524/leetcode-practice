from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            if values.get(target - nums[i]) is None:
                values[nums[i]] = i
            else:
                return [values.get(target - nums[i]), i]
        return None