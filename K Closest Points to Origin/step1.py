from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        counter = 0
        for point in points:
            dist = -(point[0] ** 2 + point[1] ** 2)
            if len(queue) < k:
                heapq.heappush(queue, (dist, counter, point))
            elif queue[0][0] < dist:
                heapq.heappop(queue)
                heapq.heappush(queue, (dist, counter, point))
            counter += 1
        
        return [p for _, _, p in queue]