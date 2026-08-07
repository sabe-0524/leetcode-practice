from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        count_t = Counter(t)
        count_s = Counter()
        answer = ""
        left = 0
        
        for right, ch in enumerate(s):
            count_s[ch] += 1
             
            while count_t <= count_s:
                if not answer or len(answer) > right - left + 1:
                    answer = s[left:right + 1]
                count_s[s[left]] -= 1
                left += 1
        
        return answer