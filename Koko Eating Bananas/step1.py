from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            middle = (left + right) // 2
            needed_hours = 0
            for pile in piles:
                needed_hours += math.ceil(pile / middle)
            
            if needed_hours > h:
                left = middle + 1
            else:
                right = middle
        
        return left