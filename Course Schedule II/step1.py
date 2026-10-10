from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        graph = [[] for _ in range(numCourses)]
        counts = [0] * numCourses
        result = []
        
        for post, pre in prerequisites:
            graph[pre].append(post)
            counts[post] += 1
        
        for i, count in enumerate(counts):
            if count == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            result.append(current)
            for nxt in graph[current]:
                counts[nxt] -= 1
                if counts[nxt] == 0:
                    queue.append(nxt)
        
        return result if len(result) == numCourses else []
        