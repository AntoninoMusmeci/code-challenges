#https://leetcode.com/problems/longest-substring-without-repeating-characters/editorial/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        characters = {}
        l = 0
        r = 0
        result = 0
        while r < len(s):
            if s[r] in characters and characters[s[r]] >= l:
                l = characters[s[r]] + 1
            characters[s[r]] = r
            result = max(result, r-l + 1)
            r += 1
        return result