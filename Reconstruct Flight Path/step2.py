from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f, t in tickets:
            graph[f].append(t)
        
        for u in graph:
            graph[u].sort(reverse=True)
        
        route = []

        def dfs(u):
            while graph[u]:
                v = graph[u].pop()
                dfs(v)
            route.append(u)
        
        dfs("JFK")
        route.reverse()
        return route
        