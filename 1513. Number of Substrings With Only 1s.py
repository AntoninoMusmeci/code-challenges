# https://leetcode.com/problems/number-of-substrings-with-only-1s/description/
class Solution:
    def numSub(self, s: str) -> int:
        result = 0
        count_ones = 0
        for i in range(len(s)):
            if s[i] == "0":
                result += count_ones*(count_ones + 1)//2
                count_ones = 0
            if s[i] == "1":
                count_ones += 1
        mod = 10**9 + 7
        return (result + count_ones*(count_ones + 1)//2) % mod
