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
        serialized = []
        queue = deque()
        queue.append(root)
        
        while queue:
            if all(v == None for v in queue):
                break
            for _ in range(len(queue)):
                target = queue.popleft()
                if target == None:
                    queue.append(None)
                    queue.append(None)
                    serialized.append("null")
                else:
                    queue.append(target.left)
                    queue.append(target.right)
                    serialized.append(str(target.val))
        
        return ",".join(serialized)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        idx = 1
        vals = data.split(",")
        queue = deque()
        head = TreeNode(int(vals[0]))
        queue.append(head)
        
        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node:
                    if idx < len(vals):
                        left_val = int(vals[idx]) if vals[idx] != "null" else None
                        left_node = TreeNode(left_val) if left_val else None
                        current_node.left = left_node
                        queue.append(left_node)
                    idx += 1
                    if idx < len(vals):
                        right_val = int(vals[idx]) if vals[idx] != "null" else None
                        right_node = TreeNode(right_val) if right_val else None
                        current_node.right = right_node
                        queue.append(right_node)
                    idx += 1
                
                else:
                    if idx < len(vals):
                        queue.append(None)
                        idx += 1
                    if idx < len(vals):
                        queue.append(None)
                        idx += 1
                
        return head
                
