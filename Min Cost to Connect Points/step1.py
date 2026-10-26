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
        
        h = [(0, 0, 0)]
        dist = [float("inf")] * len(points)
        dist[0] = 0
        result = 0
        while h:
            d, u, v = heapq.heappop(h)
            if d > dist[v]:
                continue
            
            result += graph[u][v]
            
            for i in range(len(points)):
                if i == v:
                    continue
                nd = d + graph[v][i]
                if nd < dist[i]:
                    dist[i] = nd
                    heapq.heappush(h, (nd, v, i))
        
        return result
            
        