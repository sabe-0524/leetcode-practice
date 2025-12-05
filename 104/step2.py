from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if node is None:
                continue
            max_depth = max(max_depth, depth)
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        
        return max_depth
            