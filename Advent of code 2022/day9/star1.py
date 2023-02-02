visited = set()
h = t = (0,0)

with open('day9/input.txt') as f:
     for line in f:
          line = line.strip('\n').split(" ")
          dir = line[0]
          pos = int(line[1])
        
          for _ in range(pos):
               prev_h = h
               h = h[0] + (dir == "R") - (dir == "L") , h[1] + (dir == "D") - (dir == "U")
               if max(abs(t[0] - h[0]),abs(t[1]-h[1])) == 2:
                    t = prev_h
               visited.add(t)
     print(len(visited))