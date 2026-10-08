from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rotten = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        result = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if fresh_count == 0:
            return 0
        while rotten:
            if fresh_count == 0:
                return result
            result += 1
            for _ in range(len(rotten)):
                ci, cj = rotten.popleft()
                for di, dj in directions:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_count -= 1
                        rotten.append((ni, nj))
        
        return -1