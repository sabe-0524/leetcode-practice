from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    continue
                queue = deque()
                seen = set()
                queue.append((i, j))
                seen.add((i, j))
                dist = 0
                while queue:
                    for _ in range(len(queue)):
                        ci, cj = queue.popleft()
                        grid[ci][cj] = min(grid[ci][cj], dist)
                        for di, dj in directions:
                            ni = ci + di
                            nj = cj + dj
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not (ni, nj) in seen and grid[ni][nj] > 0:
                                queue.append((ni, nj))
                                seen.add((ni, nj))
                    
                    dist += 1