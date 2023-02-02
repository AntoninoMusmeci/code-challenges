import collections, math
visited = set()
grid = []
result = math.inf
def bfs(grid, start,target):
    queue = collections.deque([start])
    seen = set(start)
    while queue:
        r, c, steps = queue.popleft()
        current_value = "a" if grid[r][c] == "S" else grid[r][c]
        if (r,c) in seen:
            continue
        seen.add((r,c))
        if current_value == target:
            return steps
        for r2, c2 in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
            if 0 <= r2 < len(grid) and 0 <= c2 < len(grid[0]):
                next_char = "z" if grid[r2][c2] == "E" else grid[r2][c2]
                if  ord(next_char) <= ord(current_value) + 1 :
                    queue.append((r2, c2, steps + 1))
    
with open('day12/input.txt') as f:
     for line in f:
          line = line.strip('\n')
          line = [c for c in line]
          grid.append(line)
          m = len(grid)
          n = len(grid[0])
          count = 0
     for r in range(m):
          for c in range(n):
               if grid[r][c] == "S" or grid[r][c] == "a":
                    steps = bfs(grid,(r,c,0),'E')
                    if steps:
                        result = min(result, steps)
     print(result)
                   
                   












            
