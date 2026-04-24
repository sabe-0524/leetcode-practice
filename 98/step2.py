# 動くけど遅い

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addList(self, root, arr):
        if root.left:
            self.addList(root.left, arr)
        arr.append(root.val)
        if root.right:
            self.addList(root.right, arr)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        arr = []
        self.addList(root, arr)
        return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))