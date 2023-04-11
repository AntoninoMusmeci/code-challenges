#https://leetcode.com/problems/removing-stars-from-a-string/description/
class Solution:
    def removeStars(self, s: str) -> str:
        nstars = 0
        result = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == "*":
                nstars += 1
            if s[i] != "*":
                if nstars > 0:
                    nstars -= 1
                else:
                    result = s[i] + result
            i -= 1
        return result