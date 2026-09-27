from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        
        def _recurSearch(node: Optional[TreeNode]):
            nonlocal max_length
            if not node:
                return 0
            
            left_length = _recurSearch(node.left)
            right_length = _recurSearch(node.right)
            
            max_length = max(max_length, left_length + right_length)
            return max(left_length, right_length) + 1
        
        _recurSearch(root)
        return max_length
