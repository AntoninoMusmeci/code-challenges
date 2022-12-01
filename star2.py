
total = 0
with open('input.txt') as f:
    result = [0,0,0]
    for line in f:
        line = line.strip('\n')
        if line:
            total += int(line)
        else:
            for i in range(1,4):
                if result[-i] < total:
                    total, result[-i] = result[-i], total
            total = 0
    if total:
        for i in range(1,4):
            if result[-i] < total:
                total, result[-i] = result[-i], total
    print(result)
    print(sum(result))