class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        n -= 1
        current = 0
        while n > 0:
            half = 2 ** (n - 1)
            if k > half:
                k -= half
                current = 1 - current
            n -= 1
        
        return current
                
