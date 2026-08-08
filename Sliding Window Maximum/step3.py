from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        q = deque()
        
        for right, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()
            
            if q and q[0] < right - k + 1:
                q.popleft()
            
            q.append(right)
            
            if right >= k - 1:
                answer.append(nums[q[0]])
        
        return answer