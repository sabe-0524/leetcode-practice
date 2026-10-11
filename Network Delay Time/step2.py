from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, t in times:
            graph[u].append((v, t))
        
        heap = []
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        heap.append((0, k))
        
        while heap:
            current_dist, current = heapq.heappop(heap)
            if current_dist > dist[current]:
                continue
            
            for nxt, time in graph[current]:
                nxt_dist = current_dist + time
                if dist[nxt] > nxt_dist:
                    dist[nxt] = nxt_dist
                    heapq.heappush(heap, (nxt_dist, nxt))
        
        result = max(dist[1:])
        return result if result != float("inf") else -1