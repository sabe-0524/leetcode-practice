from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        max_profit = 0
        prev = prices[0]
        for price in prices[1:]:
            profit = max(profit + price - prev, 0)
            max_profit = max(max_profit, profit)
            prev = price
        
        return max_profit