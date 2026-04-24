from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = {}
        answer = []
        counter = 0
        for text in strs:
            hashed_text = hash(tuple(sorted(text)))
            if hashed_text in hash_dict:
                answer[hash_dict[hashed_text]].append(text)
            else:
                hash_dict[hashed_text] = counter
                counter += 1
                answer.append([text])
        return answer