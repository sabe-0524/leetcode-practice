from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer: List[List[int]] = []
        q = deque([(root, 0)])
        while q:
            level_vals = []
            for _ in range(len(q)):
                node, level = q.popleft()
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
                level_vals.append(node.val)
            answer.append(level_vals)
        
        return answer