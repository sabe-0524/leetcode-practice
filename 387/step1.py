OVERRAP = 100001

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_character = {}
        for i, c in enumerate(s):
            if c in unique_character:
                unique_character[c] = OVERRAP
            else:
                unique_character[c] = i
        
        min_index = min(unique_character.values())
        if min_index == OVERRAP:
            return -1
        return min_index