class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_length = 0
        start_index = 0
        for i in range(len(s)):
            index = s[start_index:i].find(s[i])
            if index == -1:
                current_length += 1
            else:
                start_index += (index + 1)
                current_length = i - start_index + 1
            max_length = max(max_length, current_length)
        
        return max_length
                
