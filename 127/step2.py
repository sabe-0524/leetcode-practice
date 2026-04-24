from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        all_comb_dict = defaultdict(list)
        L = len(beginWord)
        
        for word in wordList:
            for i in range(L):
                generic_word = word[:i] + '*' + word[i+1:]
                all_comb_dict[generic_word].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            current, step = q.popleft()
            for i in range(len(current)):
                generic_word = current[:i] + '*' + current[i+1:]
                for next_word in all_comb_dict[generic_word]:
                    if next_word in visited:
                        continue
                    if next_word == endWord:
                        return step + 1
                    visited.add(next_word)
                    q.append((next_word, step + 1))
        return 0