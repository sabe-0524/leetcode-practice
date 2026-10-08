from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        dist = 1
        while queue:
            for _ in range(len(queue)):
                ci, cj = queue.popleft()
                for di, dj in directions:
                    ni = ci + di
                    nj = cj + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 2147483647:
                        queue.append((ni, nj))
                        grid[ni][nj] = dist
            dist += 1