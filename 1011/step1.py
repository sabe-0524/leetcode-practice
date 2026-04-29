from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkCanShip(capacity):
            current = 0
            max_days = 1
            for weight in weights:
                if weight > capacity:
                    return False
                current += weight
                if current > capacity:
                    max_days += 1
                    current = weight
            return max_days <= days
        left = 0
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if checkCanShip(mid):
                right = mid
            else:
                left = mid + 1
        return left