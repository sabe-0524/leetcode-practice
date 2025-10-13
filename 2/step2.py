from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_flag = False
        dummy = ListNode()
        prev = dummy
        while l1 or l2:
            sum_ = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0)
            if carry_flag:
                sum_ += 1
                carry_flag = False
            if sum_ >= 10:
                carry_flag = True
                sum_ -= 10
            new_node = ListNode(sum_, None)
            prev.next = new_node
            prev = prev.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry_flag:
            extra_node = ListNode(1, None)
            prev.next = extra_node
        return dummy.next or dummy
        