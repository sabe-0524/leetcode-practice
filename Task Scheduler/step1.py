from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap = [[-v, k] for k, v in c.items()]
        heapq.heapify(heap)
        idle = deque()
        cycle = 0
        
        while heap or idle:
            while idle:
                if cycle - idle[0][1] <= n:
                    break
                comeback_task = idle.popleft()
                heapq.heappush(heap, comeback_task[0])
            if heap:
                next_task = heapq.heappop(heap)
                next_task[0] += 1
                if next_task[0] < 0:
                    idle.append((next_task, cycle))
            cycle += 1

        return cycle