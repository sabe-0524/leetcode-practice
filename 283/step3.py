from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_index = 0
        for num in nums:
            if num != 0:
                nums[insert_index] = num
                insert_index += 1
        
        for i in range(insert_index, len(nums)):
            nums[i] = 0