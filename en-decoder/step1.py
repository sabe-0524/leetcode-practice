from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        answer = []
        index = 0
        next_len = 0
        while index < len(s):
            if s[index].isdigit():
                next_len = next_len * 10 + int(s[index])
                index += 1
            if s[index] == '#':
                answer.append(s[index + 1: index + next_len + 1])
                index += (next_len + 1)
                next_len = 0
        
        return answer
            
