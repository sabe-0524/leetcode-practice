from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def recurReverse(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]: 
        if not curr:
            return prev
        newHead = curr
        next = curr.next
        if next:
            newHead = self.recurReverse(curr, next)
        curr.next = prev
        return newHead
          
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurReverse(None, head)