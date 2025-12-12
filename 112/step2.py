from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node: Optional[TreeNode], current_val):
            current_val += node.val
            if not node.right and not node.left:
                return current_val == targetSum
            
            if node.left and dfs(node.left, current_val):
                return True    
            if node.right and dfs(node.right, current_val):
                return True
            
            return False
          
        return dfs(root, 0)