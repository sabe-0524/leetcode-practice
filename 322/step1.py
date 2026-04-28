from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        least_coins = [-1] * (amount + 1)
        least_coins[0] = 0
        for i in range(1, amount + 1):
            current = []
            for coin in coins:
                if i < coin:
                    continue
                if least_coins[i - coin] != -1:
                    current.append(least_coins[i - coin] + 1)
            if len(current) > 0:
                least_coins[i] = min(current)
        
        return least_coins[-1]
