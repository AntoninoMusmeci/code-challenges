visited = set()
rope_len = 10
rope = [(0,0)] * rope_len

with open('day9/input.txt') as f:
     for line in f:
          line = line.strip('\n').split(" ")
          dir = line[0]
          pos = int(line[1])
        
          for _ in range(pos):
                prev = rope[0]
                rope[0] = rope[0][0] + (dir == "R") - (dir == "L") , rope[0][1] + (dir == "D") - (dir == "U")
                
                for i in range(1,rope_len):
                    h = rope[i - 1]
                    t = rope[i]
                    if max(abs(t[0] - h[0]),abs(t[1]-h[1])) == 2:
                       t = t[0] + (t[0] < h[0]) - (t[0] > h[0]), t[1] + (t[1] < h[1]) - (t[1] > h[1])
                       
                    rope[i] = t
                visited.add(rope[-1])
     print(len(visited))