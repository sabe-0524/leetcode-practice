from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                j = i - len(word)
                if j < -1:
                    continue
                if (j == -1 or dp[j] == True) and s[j + 1:i + 1] == word:
                    dp[i] = True
        
        return dp[-1]