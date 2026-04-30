from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        index = 0
        while index < len_nums:
            if nums[index] == 0:
                del nums[index]
                len_nums -= 1
                nums.append(0)
            else:
                index += 1