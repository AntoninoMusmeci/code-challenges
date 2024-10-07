with open('input.txt') as f:
    tot = 0
    for line in f:
        l = 0
        r = len(line) - 1
        digit = [None,None]
        while not digit[0] or not digit[1]:
            if line[l].isnumeric() and not digit[0]:
                digit[0] = line[l]
            if line[r].isnumeric() and not digit[1]:
                digit[1] = line[r]
            l+= 1
            r-= 1
        
        tot += int(''.join(digit))
        print(tot)
    print(tot)
        
                
        
    #     if line:
    #         total += int(line)
    #     else:
    #         max_calories = max(max_calories, total)
    #         total = 0
    # if total:
    #     max_calories = max(max_calories, total)
    # print(max_calories)