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
        
        def search(root: Optional[TreeNode], current_sum: int):
            current_sum += root.val
            if current_sum == targetSum and not root.left and not root.right:
                return True
            left = right = False
            if root.left:
                left = search(root.left, current_sum)
            if root.right:
                right = search(root.right, current_sum)
            return right or left
        
        return search(root, 0)

        