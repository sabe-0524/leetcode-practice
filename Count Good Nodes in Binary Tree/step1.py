class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def _recurCount(node, max_num):
            nonlocal count
            if not node:
                return
            
            if node.val >= max_num:
                count += 1
                max_num = node.val
            
            _recurCount(node.left, max_num)
            _recurCount(node.right, max_num)
        
        _recurCount(root, -float('inf'))
        return count