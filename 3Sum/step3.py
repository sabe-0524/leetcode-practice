from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return answer