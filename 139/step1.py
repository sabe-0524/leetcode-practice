from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakLine(line: str, words: List[str]) -> bool:
          index = [0] * len(words)
          clear = [False] * len(words)
          for c in s:
              for i in range(len(words)):
                  if clear[i] == False and c == words[i][index[i]]:
                      index[i] += 1
                      if index[i] == len(words[i]):
                          clear[i] = True
                          index = [0] * len(words)
                  else:
                      index[i] = 0
          return all(clear)
        return wordBreakLine(s, wordDict) or wordBreakLine(s[::-1], [word[::-1] for word in wordDict])
      