from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "O":
                    continue
                seen = set()
                queue = deque()
                seen.add((i, j))
                queue.append((i, j))
                flag = True
                while queue:
                    if not flag:
                        break
                    ci, cj = queue.popleft()
                    if ci == 0 or ci == len(board) - 1 or cj == 0 or cj == len(board[0]) - 1:
                        flag = False
                        break
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in seen and board[ni][nj] == "O":
                            if ni == 0 or ni == len(board) - 1 or nj == 0 or nj == len(board[0]) - 1:
                                flag = False
                                break
                            queue.append((ni, nj))
                            seen.add((ni, nj))
                
                if flag:
                    for ti, tj in seen:
                        board[ti][tj] = "X"