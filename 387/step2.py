class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_map = {}
        for i, c in enumerate(s):
            if c in index_map:
                index_map[c] = float('inf')
            else:
                index_map[c] = i
        min_index = min(index_map.values(), default=float('inf'))
        
        return -1 if min_index == float('inf') else min_index