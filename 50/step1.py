class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1
        if n >= 0:
            for _ in range(n):
                answer *= x
        else:
            for _ in range(-n):
                answer /= x
        return answer