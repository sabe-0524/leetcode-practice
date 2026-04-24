from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:  
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            index = (left + right) // 2
            node = TreeNode(nums[index])
            if index > left:
                node.left = build(left, index - 1)
            if index < right:
                node.right = build(index + 1, right)
            return node
          
        if not nums:
            return None
        return build(0, len(nums) - 1)