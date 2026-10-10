from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indgrees = [0] * numCourses
        d = defaultdict(list)
        
        for pre, post in prerequisites:
            indgrees[post] += 1
            d[pre].append(post)
        
        queue = deque()
        t_sorted = 0
        
        for i, indgree in enumerate(indgrees):
            if indgree == 0:
                queue.append(i)
                t_sorted += 1
        
        while queue:
            current = queue.popleft()
            for nxt in d[current]:
                indgrees[nxt] -= 1
                if indgrees[nxt] == 0:
                    queue.append(nxt)
                    t_sorted += 1
        
        return t_sorted == numCourses