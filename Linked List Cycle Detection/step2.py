from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False