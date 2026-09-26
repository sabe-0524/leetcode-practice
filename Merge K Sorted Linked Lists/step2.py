from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _add(self, base, target):
        target.next = base.next
        if base.next:
            base.next.prev = target
        target.prev = base
        base.next = target
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        base = lists[0]
        for node in lists[1:]:
            current = base
            while node:
                if current.next is None:
                    current.next = node
                    break
                if current.val <= node.val and node.val < current.next.val:
                    next_node = node.next
                    self._add(current, node)
                    node = next_node
                current = current.next
        
        return base
                    
