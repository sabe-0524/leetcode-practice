from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {
            val : i for i, val in enumerate(inorder)
        }
        if not preorder:
            return None
        
        target = preorder[0]
        idx = inorder_idx[target]
        next_inorder_left = inorder[:idx]
        next_inorder_right = inorder[idx + 1:]
        next_preorder_left = preorder[1:1 + len(next_inorder_left)]
        next_preorder_right = preorder[1 + len(next_inorder_left):]
        
        new = TreeNode(target)
        new.left = self.buildTree(next_preorder_left, next_inorder_left)
        new.right = self.buildTree(next_preorder_right, next_inorder_right)
        
        return new