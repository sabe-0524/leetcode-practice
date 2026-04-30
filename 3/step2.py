class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_length = 0
        start_index = 0
        for i in range(len(s)):
            if s[i] in last_seen and last_seen[s[i]] >= start_index:
                start_index = last_seen[s[i]] + 1
            max_length = max(max_length, i - start_index + 1)
            last_seen[s[i]] = i
        
        return max_length
            
                
