from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        count_t = Counter(t)
        count_s = Counter()
        left = 0
        answer_left = 0
        answer_right = len(s) + 1
        
        for right, ch in enumerate(s):
            count_s[ch] += 1
             
            while count_t <= count_s:
                if answer_right - answer_left > right - left:
                    answer_left = left
                    answer_right = right
                count_s[s[left]] -= 1
                left += 1
        
        return s[answer_left:answer_right + 1] if answer_right != len(s) + 1 else ""