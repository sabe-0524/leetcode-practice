from typing import Optional
import ast

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while (head):
            if (head in visited):
                return True
            visited.add(head)
            head = head.next
        return False

        
if __name__ == "__main__":
    head = ast.literal_eval(input().strip())
    pos = int(input().strip())
    first: ListNode = None
    last: ListNode = None
    pos_node = None
    for i in range(len(head)):
        if i == 0:
            first = ListNode(head[i])
            last = first
        else:
            last.next = ListNode(head[i])
            last = last.next
        if (i == pos):
            pos_node = last
    last.next = pos_node
    solution = Solution()
    print(solution.hasCycle(first))
