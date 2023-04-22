#https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/?orderBy=most_votes
class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        reverse = s[::-1]
        n = len(s)
        table = [[0 for i in range(n+1)] for j in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):

                table[i][j] = max(table[i-1][j], table[i][j-1],
                                  (table[i - 1][j-1] + int(s[i-1] == reverse[j-1])))

        return n - table[-1][-1]
