from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        for num in nums:
            if len(queue) < k:
                heapq.heappush(queue, num)
            elif queue[0] < num:
                heapq.heapreplace(queue, num)
        
        return queue[0]