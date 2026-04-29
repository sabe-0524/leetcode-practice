class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        else:
            return self.myPow(x * x, n // 2) * (x if n % 2 == 1 else 1)