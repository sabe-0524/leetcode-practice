from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        current = 0
        max_count = 0
        count = defaultdict(int)
        left = 0
        right = 0
        while right < len(s):
            if current - max_count > k:
                current -= 1
                count[s[left]] -= 1
                left += 1
            else:
                current += 1
                count[s[right]] += 1
                max_count = max(count[s[right]], max_count)
                right += 1
                longest = max(longest, current)

        return longest
