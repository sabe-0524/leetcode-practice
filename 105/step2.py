from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        pre_i = 0
        
        def dfs(in_l, in_r):
            if in_l >= in_r:
                return None
            nonlocal pre_i
            root_val = preorder[pre_i]
            root = TreeNode(root_val)
            pre_i += 1
            mid = idx[root_val]
            root.left = dfs(in_l, mid)
            root.right = dfs(mid + 1, in_r)
            
            return root
          
        return dfs(0, len(preorder))
            