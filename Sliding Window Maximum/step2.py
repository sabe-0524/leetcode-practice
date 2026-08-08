from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sorted_pairs = sorted(enumerate(nums), key=lambda x:x[1])
        answer = [0] * (len(nums) - k + 1)
        for index, num in sorted_pairs:
            left = max(0, index - k + 1)
            right = min(index + k - 1, len(answer))

            answer[left:right] = [num] * (right - left)
        
        return answer