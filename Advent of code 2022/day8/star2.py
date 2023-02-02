
def compute_score(input,i,j):
    score = 1
    DIR = [(-1,0),(0,1),(1,0),(0,-1)]
    for (dr,dc) in DIR:
        R = len(input[0])
        C = len(input)
        dist = 1
        r = i+dr
        c = j+dc
        while True:
            if not (0<=r<R and 0<=c<C):
                dist -= 1
                break
            if input[r][c]>=input[i][j]:
                break
            dist += 1
            r += dr
            c += dc
        score *= dist
    return score

input = []
max_score = 0
with open('day8/input.txt') as f:
     for line in f:
          line = line.strip('\n')
          line = [int(n) for n in line]
          input.append(line)
for i in range(1,len(input) - 1):
    for j in range(1,len(input[0]) - 1):
        max_score = max(max_score,compute_score(input,i,j))
print(max_score)





