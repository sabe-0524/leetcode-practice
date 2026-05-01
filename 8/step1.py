class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        flag = 1
        index = 0
        while index < len(s) and s[index] == " ":
            index += 1
        if index < len(s) and (s[index] == "+" or s[index] == "-"):
            if s[index] == "-":
                flag = -1
            index += 1
        while index < len(s) and "0" <= s[index] <= "9":
            answer = answer * 10 + int(s[index])
            index += 1
        INT_MIN = - (2 ** 31)
        INT_MAX = 2 ** 31 - 1
        return max(INT_MIN, min(INT_MAX, answer * flag))