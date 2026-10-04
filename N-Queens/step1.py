from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = []
        board = [[False] * n for _ in range(n)]
        
        def can_place(i, j):
            for k in range(n):
                if board[i][k] or board[k][j]:
                    return False
                if i + k < n and j + k < n and board[i + k][j + k]:
                    return False
                if i + k < n and j - k >= 0 and board[i + k][j - k]:
                    return False
                if i - k >= 0 and j + k < n and board[i - k][j + k]:
                    return False
                if i - k >= 0 and j - k >= 0 and board[i - k][j - k]:
                    return False
            return True
        
        def backtrack(i):
            if i == n:
                result.append(path.copy())
                return
            
            for j in range(n):
                if can_place(i, j):
                    board[i][j] = True
                    path.append("." * j + "Q" + "." * (n - j - 1))
                    backtrack(i + 1)
                    path.pop()
                    board[i][j] = False

        backtrack(0)
        return result