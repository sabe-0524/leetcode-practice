from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen_ver = set()
            seen_hor = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in seen_ver:
                        return False
                    seen_ver.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in seen_hor:
                        return False
                    seen_hor.add(board[j][i])
        def check_squire(start_left, start_up):
            seen = set()
            for i in range(start_left, start_left + 3):
                for j in range(start_up, start_up + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        for i in range(3):
            for j in range(3):
                if not check_squire(i * 3, j * 3):
                    return False
        
        return True
