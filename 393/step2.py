from typing import List
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
                
        visited = [False for _ in range(n)]
        q = deque()
        count = 0
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            count += 1
            q.append(i)
            while q:
                current = q.popleft()
                for neighbor in graph[current]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    q.append(neighbor)
        
        return count