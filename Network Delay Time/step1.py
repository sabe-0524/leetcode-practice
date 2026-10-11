from typing import List
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, t in times:
            graph[u].append((v, t))
        
        requires = [float("inf")] * (n + 1)
        queue = deque()
        queue.append(k)
        requires[k] = 0
        
        while queue:
            current = queue.popleft()
            for nxt, time in graph[current]:  
                if requires[nxt] > requires[current] + time:
                    requires[nxt] = requires[current] + time
                    queue.append(nxt)
        
        result = max(requires[1:])
        return result if result != float("inf") else -1