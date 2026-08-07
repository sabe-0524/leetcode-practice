from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = Counter()
        answer = ""
        left = 0
        right = 0
        while right < len(s):
            if count_t <= count_s:
                if answer == "" or len(answer) > right - left:
                    answer = s[left:right]
                count_s[s[left]] -= 1
                left += 1
            else:
                count_s[s[right]] += 1
                right += 1
                
        return answer