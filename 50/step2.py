class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_abs = abs(n)
        two_pow_list = []
        two_pow = 1
        while two_pow <= n_abs:
            two_pow_list.append(two_pow)
            two_pow *= 2
        x_pow_list = []
        for _ in two_pow_list:
            x_pow_list.append(x)
            x *= x
        answer = 1
        for i in range(len(two_pow_list) - 1, -1, -1):
            if two_pow_list[i] <= n_abs:
                if n >= 0:
                    answer *= x_pow_list[i]
                else:
                    answer /= x_pow_list[i]
                n_abs -= two_pow_list[i]
        
        return answer