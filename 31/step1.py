from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        while index > 0 and nums[index - 1] >= nums[index]:
            index -= 1
        if index == 0:
            nums.reverse()
            return
        change_index = index - 1
        min_index = index
        for i in range(index, len(nums)):
            if nums[i] > nums[change_index]:
                min_index = i if nums[i] < nums[min_index] else min_index
        nums[min_index], nums[change_index] = nums[change_index], nums[min_index]
        nums[change_index + 1:] = sorted(nums[change_index + 1:])

        