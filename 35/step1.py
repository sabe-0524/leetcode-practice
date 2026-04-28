from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            index = (left + right) // 2
            if nums[index] < target:
                left = index + 1
            elif nums[index] > target:
                right = index - 1
            else:
                return index
        
        if nums[left] >= target:
            return left
        else:
            return left + 1