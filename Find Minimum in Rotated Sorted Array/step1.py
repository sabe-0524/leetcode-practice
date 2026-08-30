from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle
        
        return nums[left]