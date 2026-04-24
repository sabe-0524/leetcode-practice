from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for text in strs:
            key = tuple(sorted(text))
            anagram_map[key].append(text)
        return list(anagram_map.values())