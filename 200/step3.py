from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        
        rows, cols = len(grid), len(grid[0])
        
        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            move_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in move_dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    count += 1
                    
        return count
            
