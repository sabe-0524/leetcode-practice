from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 is not None or l2 is not None or carry:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            total = num1 + num2 + carry
            carry = total // 10
            new_node = ListNode(total % 10)
            tail.next = new_node
            tail = tail.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next or dummy