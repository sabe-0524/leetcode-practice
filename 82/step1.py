from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        last = None
        has_dupli = False
        while current and current.next:
            while current.next and current.val == current.next.val:
                has_dupli = True
                current = current.next
            if has_dupli:
                if last is None:
                    head = current.next
                else:
                    last.next = current.next
            else:
                last = current
            current = current.next
            has_dupli = False
        return head
        