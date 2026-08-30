from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[left] <= nums[middle]:
                if nums[left] <= target and target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[left] <= target or target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
        
        return left if nums[left] == target else -1