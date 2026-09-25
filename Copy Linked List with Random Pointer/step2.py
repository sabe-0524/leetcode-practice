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
        dummy = Node(0, head, None)
        new_dummy = Node(0, None, None)
        
        current = dummy
        new_current = new_dummy
        while current:
            if current.next:
                if current.next in seen:
                    new_current.next = seen[current.next]
                else:
                    new = Node(current.next.val, None, None)
                    seen[current.next] = new
                    new_current.next = new
            
            if current.random:
                if current.random in seen:
                    new_current.random = seen[current.random]
                else:
                    new = Node(current.random.val, None, None)
                    seen[current.random] = new
                    new_current.random = new
            
            current = current.next
            new_current = new_current.next
        
        return new_dummy.next