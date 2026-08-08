from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        current_position, max_num = max(enumerate(nums[:k]), key=lambda x:x[1])
        answer.append(max_num)

        for i in range(k, len(nums)):
            new_num = nums[i]
            if new_num >= max_num:
                max_num = new_num
                current_position = i
            
            if current_position < i - k + 1:
                current_position, max_num = max(enumerate(nums[i - k + 1:i + 1]), key=lambda x:x[1])
            
            answer.append(max_num)
        
        return answer
                