from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        path = []
        
        def backtrack(idx):
            if idx == len(digits):
                if idx > 0:
                    result.append("".join(path))
                return
            
            candidates = letter[digits[idx]]
            for candidate in candidates:
                path.append(candidate)
                backtrack(idx + 1)
                path.pop()
        
        backtrack(0)
        return result
