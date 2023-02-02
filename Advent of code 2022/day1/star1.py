max_calories = 0
total = 0
with open('input.txt') as f:
    
    for line in f:
        line = line.strip('\n')
        if line:
            total += int(line)
        else:
            max_calories = max(max_calories, total)
            total = 0
    if total:
        max_calories = max(max_calories, total)
    print(max_calories)