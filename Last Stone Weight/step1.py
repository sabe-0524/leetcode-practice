from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            heavier = heapq.heappop(stones)
            lighter = heapq.heappop(stones)
            
            if heavier != lighter:
                heapq.heappush(stones, heavier - lighter)
        
        return -stones[0] if stones else 0