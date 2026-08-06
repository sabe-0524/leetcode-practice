from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = defaultdict(int)
        current = 0
        longest = 0
        max_count = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            max_count = max(max_count, count[ch])
            current = right - left + 1
            if current - max_count > k:
                count[s[left]] -= 1
                left += 1
                continue
            
            longest = max(longest, current)
        
        return longest