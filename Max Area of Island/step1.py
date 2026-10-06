from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = [[False] * len(row) for row in grid]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] or grid[i][j] == 0:
                    continue
                seen[i][j] = True
                queue.append((i, j))
                area = 0
                while queue:
                    ci, cj = queue.popleft()
                    area += 1
                    for di, dj in directions:
                        ni = ci + di
                        nj = cj + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and seen[ni][nj] == False and grid[ni][nj] == 1:
                            queue.append((ni, nj))
                            seen[ni][nj] = True
                max_area = max(max_area, area)
        
        return max_area
                            
