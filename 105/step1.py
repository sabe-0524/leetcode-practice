# なんか色々間違っている

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def addTree(lst, next_index):
            if lst is None:
                return None
            cur_val = preorder[next_index]
            node = TreeNode(cur_val)
            lst_index = lst.index(cur_val)
            left_lst = lst[:lst_index]
            right_lst = lst[lst_index + 1:]
            
            node.left = addTree(left_lst, next_index + 1)
            node.right = addTree(right_lst, next_index + 1 + len(left_lst))
            
            return node
            
        return addTree(inorder, 0)