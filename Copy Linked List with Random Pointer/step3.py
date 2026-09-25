from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        seen = {}
        current = head
        while current:
            new = Node(current.val)
            seen[current] = new
            current = current.next
        
        current = head
        while current:
            seen[current].next = seen.get(current.next)
            seen[current].random = seen.get(current.random)
            current = current.next
        
        return seen[head]
