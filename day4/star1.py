result = 0
with open('day4/input.txt') as f:
    for line in f:
        line = line.strip('\n')
        assignments = line.split(',')
        a1 = assignments[0].split('-')
        a2 = assignments[1].split('-')
        if int(a1[0]) <= int(a2[0]) and int(a1[1]) >= int(a2[1]) \
         or int(a2[0]) <= int(a1[0]) and int(a2[1]) >= int(a1[1]):
            result += 1
    print(result)
