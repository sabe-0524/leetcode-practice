from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(lowest, price)
            answer = max(answer, price - lowest)
        return answer