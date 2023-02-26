# https://leetcode.com/problems/edit-distance/description/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # inizialize the table
        dp = [[math.inf] * (n + 1) for _ in range(m + 1)]
        # add base cases on the table

        for i in range(n+1):
            dp[m][i] = n - i
        for i in range(m+1):
            dp[i][n] = m - i

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
        return dp[0][0]
