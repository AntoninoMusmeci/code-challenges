#https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str):
        window = len(p)
        if window > len(s):
            return []
        pChars, sChars  = [0] * 26, [0] * 26
        for i in range(window):
             pChars[ord(p[i]) - ord('a')] +=1
             sChars[ord(s[i]) - ord('a')] +=1
        result = []
        start = 0
        while start  < len(s) - window:
           if sChars == pChars:
               result.append(start )
           sChars[ord(s[start]) - ord('a')] -= 1
           sChars[ord(s[start  + window]) - ord('a')] += 1  
           start +=1
        return result + [start] if sChars == pChars else result