from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(lambda: defaultdict(int))
        for u, v in tickets:
            graph[u][v] += 1
        
        def backtrack(current, path):
            if len(path) == len(tickets) + 1:
                return path
            
            for nxt in sorted(graph[current]):
                if graph[current][nxt] == 0:
                    continue
                graph[current][nxt] -= 1
                path.append(nxt)
                result = backtrack(nxt, path)
                if result:
                    return result
                graph[current][nxt] += 1
                path.pop()
            
            return []
        
        return backtrack("JFK", ["JFK"])
            