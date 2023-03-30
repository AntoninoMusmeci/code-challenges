#https://leetcode.com/problems/scramble-string/description/
from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        def scramble(s1,s2,mem):
            key = s1+s2
            if key in mem:
                return mem[key]
            if s1 == s2:
                return True

            if Counter(s1) != Counter(s2):
                return False
            
            for i in range(1,len(s1)):
                if scramble(s1[:i],s2[:i],mem) and scramble(s1[i:],s2[i:],mem) or scramble(s1[:i],s2[-i:],mem) and scramble(s1[i:],s2[:-i],mem):
                    mem[key] = True
                    return True
            mem[key] = False
            return False
        
        return scramble(s1,s2,{})