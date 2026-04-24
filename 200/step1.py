from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = [[False for _ in range(len(grid[row]))] for row in range(len(grid))]
        queue = deque()
        
        def bfs(i: int, j: int) -> None:
            if seen[i][j] == True or grid[i][j] == "0":
                return
            nonlocal count
            count += 1
            seen[i][j] = True
            while True:
                if j + 1 < len(grid[i]) and grid[i][j + 1] == "1" and seen[i][j + 1] == False:
                    queue.append((i, j + 1))
                    seen[i][j + 1] = True
                if i + 1 < len(grid) and grid[i + 1][j] == "1" and seen[i + 1][j] == False:
                    queue.append((i + 1, j))
                    seen[i + 1][j] = True
                if i > 0 and grid[i - 1][j] == "1" and seen[i - 1][j] == False:
                    queue.append((i - 1, j))
                    seen[i - 1][j] = True
                if j > 0 and grid[i][j - 1] == "1" and seen[i][j - 1] == False:
                    queue.append((i, j - 1))
                    seen[i][j - 1] = True
                if not queue:
                    break
                i, j = queue.popleft()
                seen[i][j] = True
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                bfs(i, j)
        return count