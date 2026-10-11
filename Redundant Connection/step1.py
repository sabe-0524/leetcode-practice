from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def find_root(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(a, b):
            a_root = find_root(a)
            b_root = find_root(b)
            if a_root == b_root:
                return True
            parent[a_root] = b_root
            return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        
        return []