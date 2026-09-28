from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = -float("inf")
        
        def _recurSearch(node):
            nonlocal answer
            if not node:
                return 0
            
            left_path = _recurSearch(node.left)
            right_path = _recurSearch(node.right)
            
            current_path = max(node.val, node.val + left_path, node.val + right_path)
            answer = max(answer, current_path, node.val + left_path + right_path)
            return current_path
        
        _recurSearch(root)
        return answer