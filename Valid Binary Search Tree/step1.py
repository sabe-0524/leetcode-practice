from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current = -float('inf')
        
        def dfs(node):
            nonlocal current
            if not node:
                return True
            
            if not dfs(node.left):
                return False
              
            if current >= node.val:
                return False
            current = node.val
            
            if not dfs(node.right):
                return False
              
            return True
        
        return dfs(root)