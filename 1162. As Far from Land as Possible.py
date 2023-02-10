#https://leetcode.com/problems/as-far-from-land-as-possible/
class Solution:
    def maxDistance(self, grid):
        maxDistance = -1
        dist_max = len(grid) + len(grid[0]) + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = min(dist_max, 1+ grid[i-1][j] if i-1 >= 0 else dist_max, 1+ grid[i][j-1] if j-1 >= 0 else dist_max)
              
        for i in range(len(grid) - 1, -1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j] != 1:
                    grid[i][j] = min(grid[i][j], 1 + grid[i+1][j] if i+1 < len(grid) else dist_max, 1 + grid[i][j+1] if j+1 < len(grid[0]) else dist_max)
                maxDistance = max(maxDistance, grid[i][j])
        if maxDistance == 0 or maxDistance == dist_max: return -1
        return maxDistance