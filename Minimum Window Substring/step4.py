from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        window = Counter()
        need = Counter(t)
        formed = 0
        required = len(need)
        min_length = float("inf")
        left = 0
        answer = ""
        
        for right, ch in enumerate(s):
            window[ch] += 1
            
            if ch in need and window[ch] == need[ch]:
                formed += 1
            
            while formed == required:
                left_ch = s[left]
                current = right - left + 1
                if min_length > current:
                    min_length = current
                    answer = s[left:right + 1]
                if left_ch in need and window[left_ch] == need[left_ch]:
                    formed -= 1
                window[left_ch] -= 1
                left += 1
                
        return answer