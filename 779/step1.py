class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        n -= 1
        k -= 1
        grammer = "0"
        for _ in range(n):
            grammer = grammer.replace("0", "A")
            grammer = grammer.replace("1", "B")
            grammer = grammer.replace("A", "01")
            grammer = grammer.replace("B", "10")
        return int(grammer[k])
        