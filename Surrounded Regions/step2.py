from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != "O" or (i, j) in visited:
                    continue
                
                queue = deque()
                seen = set()
                queue.append((i, j))
                seen.add((i, j))
                visited.add((i, j))
                flag = False
                
                while queue:
                    ci, cj = queue.popleft()
                    if ci == 0 or ci == rows - 1 or cj == 0 or cj == cols - 1:
                        flag = True
                    
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and board[ni][nj] == "O":
                            seen.add((ni, nj))
                            visited.add((ni, nj))
                            queue.append((ni, nj))
                
                if not flag:
                    for ti, tj in seen:
                        board[ti][tj] = "X"
                