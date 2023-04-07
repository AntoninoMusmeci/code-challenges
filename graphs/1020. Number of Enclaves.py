#https://leetcode.com/problems/number-of-enclaves/editorial/
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    land_size = 0
                    queue = deque([(i, j)])
                    boundary = False
                    while queue:
                        x, y = queue.popleft()
                        if grid[x][y] == 0:
                            continue
                        grid[x][y] = 0
                        land_size += 1
                        if (x == 0 or y == 0 or x == n-1 or y == m-1):
                            boundary = True
                        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            if x + direction[0] >= 0 and x + direction[0] < n and y + direction[1] >= 0 and y + direction[1] < m and grid[x+direction[0]][y+direction[1]] == 1:
                                queue.append(
                                    (x+direction[0], y + direction[1]))
                    if not boundary:
                        result += land_size
        return result
