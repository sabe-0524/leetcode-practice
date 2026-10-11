from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        length = len(wordList)
        graph = [[] for _ in range(length)]
        for i in range(length):
            for j in range(i + 1, length):
                diff = sum(a != b for a, b in zip(wordList[i], wordList[j]))
                if diff == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        queue = deque()
        seen = set()
        level = 1
        
        for i, word in enumerate(wordList):
            diff = sum(a != b for a, b in zip(beginWord, word))
            if diff == 1:
                queue.append(i)
                seen.add(i)
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                if wordList[current] == endWord:
                    return level
                for nxt in graph[current]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
        
        return 0