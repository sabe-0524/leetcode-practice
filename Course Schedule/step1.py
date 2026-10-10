from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for prerequisite in prerequisites:
            pre, post = prerequisite[0], prerequisite[1]
            d[pre].append(post)
            
            queue = deque(d[pre])
            seen = set()
            while queue:
                nxt = queue.popleft()
                if nxt in seen:
                    continue
                seen.add(nxt)
                if nxt == pre:
                    return False
                queue.extend(d[nxt])
        
        return True
            