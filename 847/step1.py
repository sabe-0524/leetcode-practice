
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:
        if root is None:
            return [None, None]
        if root.val <= v:
            small, large = self.split_b_s_t(root.right, v)
            root.right = small
            return [root, large]
        else:
            small, large = self.split_b_s_t(root.left, v)
            root.left = large
            return [small, root]