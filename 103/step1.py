from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        q = deque()
        if not root:
            return answer
        
        q.append(root)
        is_odd = False
        while (q):
            level_val = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if is_odd:
                    level_val.appendleft(node.val)
                else:
                    level_val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            is_odd = not is_odd
            answer.append(list(level_val))
        
        return answer
                
