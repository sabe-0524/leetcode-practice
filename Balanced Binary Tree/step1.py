from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance_flag = True
        
        def _recurSearch(node: Optional[TreeNode]):
            nonlocal balance_flag
            if not node:
                return 0
            
            left_depth = _recurSearch(node.left)
            right_depth = _recurSearch(node.right)
            
            if abs(left_depth - right_depth) > 1:
                balance_flag = False
            
            return max(left_depth, right_depth) + 1
        
        _recurSearch(root)
        return balance_flag