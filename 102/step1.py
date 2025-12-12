from typing import Optional, List
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            d[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        max_index = max(d.keys())
        answer = [[] for _ in range(max_index + 1)]
        
        for i, v in d.items():
            answer[i] = v
        
        return answer
