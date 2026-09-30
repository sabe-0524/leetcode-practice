
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque()
        serialized = []
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node is None:
                serialized.append("null")
                continue
            serialized.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ",".join(serialized)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        queue = deque()
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue.append(root)
        idx = 1
        
        while queue:
            node = queue.popleft()
            
            if vals[idx] != "null":
                node.left = TreeNode(int(vals[idx]))
                queue.append(node.left)
            
            idx += 1
            
            if vals[idx] != "null":
                node.right = TreeNode(int(vals[idx]))
                queue.append(node.right)
            
            idx += 1
        
        return root