#https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        l = 0
        r = n-1
        for i in range(n):
            for j in range(n):
                if i == j  or i == n-1 - j:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True