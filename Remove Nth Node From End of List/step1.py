from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(0, head)
        current = head
        while current:
            length += 1
            current = current.next
          
        current = dummy
        for _ in range(length - n):
            current = current.next
        
        target = current.next
        current.next = target.next if target else None

        return dummy.next