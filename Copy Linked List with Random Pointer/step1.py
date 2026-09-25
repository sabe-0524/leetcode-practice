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
        
        dummy = Node(0, None, None)
        prev = dummy
        current = head
        seen = set()
        
        while current:
            new_current = Node(current.val, None, None)
            prev.next = new_current
            prev = new_current
            current = current.next
        