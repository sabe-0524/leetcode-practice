from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _recurDepth(self, current: Optional[TreeNode], depth: int):
        if not current:
            return depth
        depth += 1
        left_depth = self._recurDepth(current.left, depth)
        right_depth = self._recurDepth(current.right, depth)
        
        return max(left_depth, right_depth)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._recurDepth(root, 0)