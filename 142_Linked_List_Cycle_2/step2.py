from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        fast = slow = head
        hascycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if (fast is slow):
                hascycle = True
                break
        if hascycle is True:
            slow = head
            while fast is not slow:
                fast = fast.next
                slow = slow.next
            return fast
        else:
            return None