class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        n -= 1
        current = False
        while n > 0:
            if not ((2 ** n) // k > 1):
                current = not current
                k -= 2 ** (n - 1)
            n -= 1
        
        return 1 if current == True else 0
