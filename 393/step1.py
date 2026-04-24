from typing import List
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        count = 0
        visited = [False for _ in range(n)]
        q = deque()
        for i in range(n):
            if visited[i] == True:
                continue
            q.append(i)
            count += 1
            while q:
                current = q.popleft()
                visited[current] = True
                for next in graph[current]:
                    if visited[next] ==  False:
                        visited[next] = True
                        q.append(next)
        
        return count
            
            
        