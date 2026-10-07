from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copied = {}
        queue = deque()
        queue.append(node)
        
        while queue:
            current = queue.popleft()
            if current in copied:
                continue
            new = Node(current.val)
            copied[current] = new
            for neighbor in current.neighbors:
                if neighbor in copied:
                    new.neighbors.append(copied[neighbor])
                    copied[neighbor].neighbors.append(new)
                else:
                    queue.append(neighbor)
        
        return copied[node]