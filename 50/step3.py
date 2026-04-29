class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        
        answer = 1
        while n > 0:
            if n % 2 == 1:
                answer *= x
            n //= 2
            x *= x
        
        return answer