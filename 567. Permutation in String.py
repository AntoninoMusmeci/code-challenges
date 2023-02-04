#https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        start = 1
        s1_char = [0] * 26
        s2_char = [0] * 26
        for c in s1:
            s1_char[ord(c) - ord('a')] +=1
        for c in s2[0:window_size]:
            s2_char[ord(c) - ord('a')] +=1
        while start + window_size <= len(s2):
            if s1_char == s2_char:
                return True
            s2_char[ord(s2[start - 1]) - ord('a')] -= 1
            s2_char[ord(s2[start + window_size - 1]) - ord('a')] += 1
            start += 1
        return s1_char == s2_char