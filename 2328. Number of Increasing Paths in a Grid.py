#https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
        result = 0
        @lru_cache(None)
        def dfs(i,j):
            # if dp[i][j] != -1: return dp[i][j]
            res = 1
            for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
                if  0 <= x < len(grid) and 0 <= y < len(grid[0]) and [grid[x][y]] > [grid[i][j]]:
                    res += dfs(x,y)
            return res
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += dfs(i,j)
        return result % (10**9 + 7)

#solution without @lru_cache

# class Solution:
#     def countPaths(self, grid: List[List[int]]) -> int:
#         dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
#         def dfs(i,j, path, vis):
#             if dp[i][j] != -1: return dp[i][j]
#             dp[i][j] = 1
#             for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
#                 if  0 <= x < len(grid) and 0 <= y < len(grid[0]) and [grid[x][y]] > [grid[i][j]]:
#                     dp[i][j] += dfs(x,y, path + [grid[x][y]], vis)
#             return dp[i][j]
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 dfs(i,j, [grid[i][j]],0)
#         return sum(sum(dp[i]) % (10**9 + 7) for i in range(len(dp))) % (10**9 + 7)

# space = O(nm) time = O(nm)