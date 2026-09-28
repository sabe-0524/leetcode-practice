from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {
            val: i for i, val in enumerate(inorder)
        }
        def _recurBuild(left, right, preorder_idx):
            
            if left >= right:
                return None
            
            target = preorder[preorder_idx]
            idx = inorder_idx[target]
            new = TreeNode(target)
            new.left = _recurBuild(left, idx, preorder_idx + 1)
            new.right = _recurBuild(idx + 1, right, preorder_idx + idx - left + 1)
            
            return new
        
        return _recurBuild(0, len(preorder), 0)