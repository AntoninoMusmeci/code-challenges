# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        
        res = 0
        n = len(s)

        for i in range(n):
            if i % 2:
                if s[i] != '0':
                    res += 1
            else:
                if s[i] != '1':
                    res += 1
        return min(res, n - res)