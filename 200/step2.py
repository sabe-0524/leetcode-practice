from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False for _ in row] for row in grid]
        queue = deque()
        def bfs(i, j, count): 
            if grid[i][j] == "0" or visited[i][j] == True:
                return count
            visited[i][j] = True
            while True:
                if i > 0 and grid[i - 1][j] == "1" and visited[i - 1][j] == False:
                    queue.append((i - 1, j))
                    visited[i - 1][j] = True
                if j > 0 and grid[i][j - 1] == "1" and visited[i][j - 1] == False:
                    queue.append((i, j - 1))
                    visited[i][j - 1] = True
                if i + 1 < len(grid) and grid[i + 1][j] == "1" and visited[i + 1][j] == False:
                    queue.append((i + 1, j))
                    visited[i + 1][j] = True
                if j + 1 < len(grid[i]) and grid[i][j + 1] == "1" and visited[i][j + 1] == False:
                    queue.append((i, j + 1))
                    visited[i][j + 1] = True
                if not queue:
                    break
                i, j = queue.popleft()
            return count + 1
                
              
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count = bfs(i, j, count)
        return count