from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            if not node:
                return -1
            
            left_value = dfs(node.left)
            if left_value != -1:
                return left_value
            
            count += 1
            if count == k:
                return node.val
            
            right_value = dfs(node.right)
            if right_value != -1:
                return right_value
            
            return -1
        
        return dfs(root)