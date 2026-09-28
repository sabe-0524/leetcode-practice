from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        def _makeList(node, level):
            if not node:
                return
            
            if len(answer) < level:
                answer.append([])
            
            answer[level - 1].append(node.val)
            _makeList(node.left, level + 1)
            _makeList(node.right, level + 1)
        
        _makeList(root, 1)
        return answer