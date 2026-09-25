from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        length = 0
        dupli = head
        while dupli:
            length += 1
            dupli = dupli.next
        
        current = head
        for _ in range((length - 1) // 2):
            current = current.next
        
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        p1 = head
        p2 = prev
        
        while p1 and p2:
            next1 = p1.next
            next2 = p2.next
            
            p1.next = p2
            p2.next = next1
            
            p1 = next1
            p2 = next2
        
        return head
            
