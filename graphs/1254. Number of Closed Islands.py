#https://leetcode.com/problems/number-of-closed-islands/editorial/
from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        result = 0
       
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if(grid[i][j]) == 0:
                    close = True
                    queue = deque([(i,j)])
                    while queue:
                        x,y = queue.popleft()
                        if(x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) -1) :
                            close = False
                        grid[x][y] = 1
                        for next in ((0,1),(1,0),(0,-1),(-1,0)):
                            if x+next[0] >= 0 and x+next[0] < len(grid) and y+next[1] >= 0 and y+next[1] <len(grid[0]):
                                if grid[x+next[0]][y+next[1]] == 0:
                                    queue.append((x+next[0], y+next[1]))
                    if close:
                        result += 1
        return result