 #https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        c_map = {}
        result = 0
        while left < len(s) and right  < len(s)  :
            c_map[s[right]] = c_map.get(s[right], 0) + 1
            if(len(c_map) == 3):
                while len(c_map) == 3:
                    result += len(s) - right
                    c_map[s[left]] -= 1 
                    if c_map[s[left]] == 0:
                        del c_map[s[left]]
                    left += 1
            right += 1
        return result 