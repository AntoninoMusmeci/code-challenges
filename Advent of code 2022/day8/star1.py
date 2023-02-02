input = []
with open('day8/input.txt') as f:
     for line in f:
          line = line.strip('\n')
          line = [int(n) for n in line]
          input.append(line)
result = 0
visible = set()
R = len(input[0])
C = len(input)
for i in range(C):
     max_height = -1
     for j in range(R):
          if input[i][j] > max_height:
               max_height = input[i][j]
               if (i,j) not in visible:
                    result += 1
                    visible.add((i,j))
     max_height = -1
     for j in range(R-1 ,-1,-1):
          if input[i][j] > max_height:
               max_height = input[i][j]
               if (i,j) not in visible:
                    result += 1
                    visible.add((i,j))
for i in range(C):
     max_height = -1
     for j in range(R):
          if input[j][i] > max_height:
               max_height = input[j][i]
               if (j,i) not in visible:
                    result += 1
                    visible.add((j,i))
     max_height = -1
     for j in range(R-1,-1,-1):
          if input[j][i] > max_height:
               max_height = input[j][i]
               if (j,i) not in visible:
                    result += 1
                    visible.add((j,i))
print(result)

def check_heigth(r,c,input,visible):
     result = 0
     if input[j][i] > max_height:
          max_height = input[j][i]
          if (j,i) not in visible:
               result = 1
               visible.add((j,i))
     return result 