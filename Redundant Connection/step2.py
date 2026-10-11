from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(a, b):
            a_root = find(a)
            b_root = find(b)
            if a_root == b_root:
                return False
            
            if size[a_root] < size[b_root]:
                a_root, b_root = b_root, a_root
            
            parent[a_root] = b_root
            size[a_root] += size[b_root]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []