from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        
        def backtrack(i, j, idx):
            if board[i][j] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True
            
            used.add((i, j))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in used:
                    if backtrack(ni, nj, idx + 1):
                        return True
            
            used.discard((i, j))
            return False
      
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        
        return False
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        for word in words:
            if self.exist(board, word):
                result.append(word)
        
        return result