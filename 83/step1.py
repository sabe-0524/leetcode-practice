from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current_node = head
        while current_node and current_node.next:
            next_node = current_node.next
            if (next_node.val == current_node.val):
                current_node.next = next_node.next
            else:
                current_node = current_node.next
        return head