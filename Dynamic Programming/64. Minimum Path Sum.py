#https://leetcode.com/problems/minimum-path-sum/description/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n - 1, -1, -1):
            for j in range(m-1,-1,-1):
                
                if i+1 < n and j+1 < m:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])
                if i+1 < n and j+1 >=m:
                    grid[i][j] =  grid[i][j] + grid[i+1][j]
                if j+1 < m and i+1 >=n:
                    grid[i][j]=grid[i][j]+ grid[i][j+1]

                
        return grid[0][0]