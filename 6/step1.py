class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        store = [[] for _ in range(numRows)]
        base = 2 * (numRows - 1)
        for i, ch in enumerate(s):
            store[min(i % base, abs(i % base - base))].append(ch)
        answer = "".join(["".join(tmp) for tmp in store])
        return answer