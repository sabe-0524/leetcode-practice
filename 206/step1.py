from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        dummy = ListNode()
        prevNode = dummy
        while stack:
            newNode = ListNode(val = stack.pop())
            prevNode.next = newNode
            prevNode = newNode
        return dummy.next
        