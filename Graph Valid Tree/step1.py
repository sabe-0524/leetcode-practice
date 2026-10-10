from typing import List
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        queue = deque()
        seen = set()
        graph = [[] for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue.append((None, 0))
        seen.add(0)
        count = 0
        
        while queue:
            prev, current = queue.popleft()
            for nxt in graph[current]:
                if nxt == prev:
                    continue
                if nxt in seen:
                    return False
                queue.append((current, nxt))
                seen.add(nxt)
            count += 1
        
        return count == n
        