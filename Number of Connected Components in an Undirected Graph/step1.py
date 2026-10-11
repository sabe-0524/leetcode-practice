from typing import List
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()
        queue = deque()
        count = 0
        
        for i in range(n):
            if i in seen:
                continue
            count += 1
            seen.add(i)
            queue.append(i)
            
            while queue:
                current = queue.popleft()
                for nxt in graph[current]:
                    if nxt in seen:
                        continue
                    queue.append(nxt)
                    seen.add(nxt)
        
        return count