from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def makeNumberFromNode(self, l: Optional[ListNode]) -> int:
        number = 0
        node = l
        weight = 1
        while node:
            number += node.val * weight
            weight *= 10
            node = node.next
        return number

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = self.makeNumberFromNode(l1)
        number2 = self.makeNumberFromNode(l2)
        sum_ = number1 + number2
        
        dummy = ListNode()
        prev = dummy
        while sum_:
            new_node = ListNode(sum_ % 10, None)
            sum_ //= 10
            prev.next = new_node
            prev = prev.next
        return dummy.next or dummy