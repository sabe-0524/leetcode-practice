from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        idx = 0
        result = False
        def backtrack(i, j):
            nonlocal idx, result
            if board[i][j] != word[idx]:
                return
            if idx == len(word) - 1:
                result = True
                return
            
            used.add((i, j))
            idx += 1
            if i + 1 < len(board) and (i + 1, j) not in used:
                backtrack(i + 1, j)
            if i > 0 and (i - 1, j) not in used:
                backtrack(i - 1, j)
            if j + 1 < len(board[0]) and (i, j + 1) not in used:
                backtrack(i, j + 1)
            if j > 0 and (i, j - 1) not in used:
                backtrack(i, j - 1)
            idx -= 1
            used.discard((i, j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j)
        return result