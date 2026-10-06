from typing import List

class Node:
    def __init__(self, word = ""):
        self.children = {}
        self.is_finish = False
        self.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            current = root
            for c in word:
                if c not in current.children:
                    current.children[c] = Node(current.word + c)
                current = current.children[c]
            current.is_finish = True
        
        result = []
        used = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def backtrack(i, j, current):
            if current.is_finish:
                current.is_finish = False
                result.append(current.word)
            
            used.add((i, j))
            
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in used:
                    nxt = board[ni][nj]
                    if nxt in current.children:
                        backtrack(ni, nj, current.children[nxt])
            
            used.discard((i, j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                head = board[i][j]
                if head in root.children:
                    backtrack(i, j, root.children[head])
        
        return result