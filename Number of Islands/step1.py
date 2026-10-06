from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = [[False] * len(row) for row in grid]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] or grid[i][j] == "0":
                    continue
                result += 1
                queue.append((i, j))
                seen[i][j] = True
                while queue:
                    ci, cj = queue.popleft()
                    for di, dj in directions:
                        ni = ci + di
                        nj = cj + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and seen[ni][nj] == False and grid[ni][nj] == "1":
                            seen[ni][nj] = True
                            queue.append((ni, nj))
                  
        
        return result