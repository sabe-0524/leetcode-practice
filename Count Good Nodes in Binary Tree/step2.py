class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_num):
            if not node:
                return 0
            
            count = 1 if node.val >= max_num else 0
            max_num = max(max_num, node.val)
            
            return count + dfs(node.left, max_num) + dfs(node.right, max_num)
        
        return dfs(root, -float('inf'))