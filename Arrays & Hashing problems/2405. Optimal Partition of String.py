#https://leetcode.com/problems/optimal-partition-of-string/description/
class Solution:
    def partitionString(self, s: str) -> int:
        char = set()
        result = 1
        for i in range(len(s)):
            if s[i] in char:
                char.clear()
                result+= 1
            char.add(s[i])
        return result