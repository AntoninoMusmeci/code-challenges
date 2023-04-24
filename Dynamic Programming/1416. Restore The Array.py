# https://leetcode.com/problems/restore-the-array/description/
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        cache = [0] * (n+1)
        def f(start):
            if cache[start]:
                return cache[start]
            tot = 0

            if start >= n:
                return 1
            if s[start] == "0":
                return 0
            for i in range(start+1, n+1):
                if int(s[start:i]) > k:
                    break
                tot += f(i) % (10**9 + 7)
            cache[start] = tot
            return tot

        return f(0) % (10**9 + 7)
