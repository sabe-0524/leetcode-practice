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
        copied = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        
        while queue:
            current = queue.popleft()
            
            for neighbor in current.neighbors:
                if neighbor not in copied:
                    new = Node(neighbor.val)
                    copied[neighbor] = new
                    queue.append(neighbor)
                copied[current].neighbors.append(copied[neighbor])
        
        return copied[node]