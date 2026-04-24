from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        count = n
        def find(i: int):
            if parent[i] == i:
                return i
            else:
                parent[i] = find(parent[i])
                return parent[i]
              
        def unite(x: int, y: int):
            nonlocal count
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            parent[root_x] = root_y
            count -= 1
            
        def same(x: int, y: int):
            return find(x) == find(y)
          
        for u, v in edges:
            unite(u, v)
        
        return count
            