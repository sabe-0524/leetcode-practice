from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        candidates = []
        count = 0
        for node in lists:
            if not node:
                continue
            heapq.heappush(candidates, (node.val, count, node))
            count += 1
        
        dummy = ListNode()
        current = dummy
        
        while candidates:
            _, counter, node = heapq.heappop(candidates)
            current.next = node
            current = current.next
            
            node = node.next
            if node is not None:
                heapq.heappush(candidates, (node.val, count, node))
                count += 1
        
        return dummy.next