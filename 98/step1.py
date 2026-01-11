# 間違い
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_flag = True
        right_flag = True
        
        if root.left:
            left_flag = self.isValidBST(root.left) and root.left.val < root.val
        if root.right:
            right_flag = self.isValidBST(root.right) and root.val < root.right.val
        
        return left_flag and right_flag
            