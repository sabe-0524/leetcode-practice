class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        seen = {}
        for right, ch in enumerate(s):
            index = seen.get(ch)
            if index is None or index < left:
                longest = max(longest, right - left + 1)
            else:
                left = index + 1
            seen[ch] = right
        
        return longest