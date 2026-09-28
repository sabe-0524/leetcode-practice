from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def _recurCheck(node, subNode):
            if not subNode and not node:
                return True
            if not node or not subNode:
                return False
            
            left_condition = _recurCheck(node.left, subNode.left)
            right_condition = _recurCheck(node.right, subNode.right)
            
            return node.val == subNode.val and left_condition and right_condition
        
        if not root:
            return False
        can_left = self.isSubtree(root.left, subRoot)
        if can_left:
            return True
        can_right = self.isSubtree(root.right, subRoot)
        if can_right:
            return True
        
        return _recurCheck(root, subRoot)
        