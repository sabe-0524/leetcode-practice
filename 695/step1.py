from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(start_r, start_c):
            area = 0
            q = deque([(start_r, start_c)])
            move_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            visited.add((start_r, start_c))
            
            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in move_dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return area
          
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = bfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area