class Solution:
    def numWays(self, n: int, k: int) -> int:
        num = []
        for i in range(n):
            if i == 0:
                num.append(k)
            elif i == 1:
                num.append(k**2)
            elif i == 2:
                num.append(k**3 - k)
            else:
                num.append(num[i - 1] * k - (num[i - 3] * (k - 1)))
        
        return num[n - 1]