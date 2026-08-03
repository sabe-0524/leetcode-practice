from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    answer.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
        
        return [list(triple) for triple in answer]
                    
