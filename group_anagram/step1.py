from typing import List, Dict
from dataclasses import dataclass

class Solution:
    @dataclass
    class Group:
        d: Dict[str, int]
        members: List[str]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: List[Solution.Group] = []
        for s in strs:
            seen = {}
            for ch in s:
                seen[ch] = seen.get(ch, 0) + 1
            for candidate in groups:
                if candidate.d == seen:
                    candidate.members.append(s)
                    break
            else:
                groups.append(Solution.Group(seen, [s]))
        
        return [group.members for group in groups]