from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            node, level = q.popleft()
            if not node:
                continue
            if not node.right and not node.left:
                return level
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        
        return 0
            