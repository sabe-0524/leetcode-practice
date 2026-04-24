from typing import List
from collections import defaultdict, deque

class Solution:
    def should_connect(self, s1: str, s2: str):
        diff_count = sum(c1 != c2 for c1, c2 in zip(s1, s2))
        if diff_count == 1:
            return True
        return False
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.insert(0, beginWord)
        for i, word1 in enumerate(wordList):
            for word2 in wordList[i + 1:]:
                if self.should_connect(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        dist = {beginWord: 1}
        q = deque()
        q.append(beginWord)
        while q:
            current = q.popleft()
            for neighbor in graph[current]:
                if neighbor in dist:
                    continue
                q.append(neighbor)
                dist[neighbor] = dist[current] + 1
                if neighbor == endWord:
                    return dist[neighbor]
        
        return 0
        