from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = [[0] * len(points) for _ in range(len(points))]
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                d = abs(xi - xj) + abs(yi - yj)
                graph[i][j] = d
                graph[j][i] = d
        
        result = 0
        seen = set()
        pq = [(0, 0, 0)]
        while pq:
            cost, f, t = heapq.heappop(pq)
            if t in seen:
                continue
            seen.add(t)
            result += cost
            
            for i in range(len(points)):
                if i == t or i in seen:
                    continue
                heapq.heappush(pq, (graph[t][i], t, i))
        
        
        return result
            
        