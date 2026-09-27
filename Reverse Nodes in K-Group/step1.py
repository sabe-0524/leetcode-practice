from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _reverse(self, node):
        current = node
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev, node
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_list = []
        current = head
        count = 0
        new_head = None
        remainder = None
        while current:
            next_node = current.next
            if count == 0:
                new_head = current
            count += 1
            if count >= k or current.next is None:
                current.next = None
                if count == k:
                    node_list.append(new_head)
                else:
                    remainder = new_head
                    
                count = 0
            
            current = next_node

        dummy = ListNode()
        current = dummy
        for node in node_list:
            start, end = self._reverse(node)
            current.next = start
            current = end
        
        current.next = remainder
        
        return dummy.next
