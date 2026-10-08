from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(len(heights[0])):
            pacific.add((0, i))
            queue.append((0, i))
        
        for i in range(1, len(heights)):
            pacific.add((i, 0))
            queue.append((i, 0))
        
        while queue:
            ci, cj = queue.popleft()
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and (ni, nj) not in pacific and heights[ni][nj] >= heights[ci][cj]:
                    pacific.add((ni, nj))
                    queue.append((ni, nj))
        
        for i in range(len(heights[0])):
            atlantic.add((len(heights) - 1, i))
            queue.append((len(heights) - 1, i))
        
        for i in range(len(heights) - 1):
            atlantic.add((i, len(heights[0]) - 1))
            queue.append((i, len(heights[0]) - 1))
        
        while queue:
            ci, cj = queue.popleft()
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and (ni, nj) not in atlantic and heights[ni][nj] >= heights[ci][cj]:
                    atlantic.add((ni, nj))
                    queue.append((ni, nj))
         
        return list(pacific & atlantic)