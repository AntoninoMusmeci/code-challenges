with open('input.txt') as f:
    scratchcards = [] 
    result = 0
    for i,line in enumerate(f):
        count = 0
        if '\n' in line:
            line = line[:-1]
        [winnings, tries] = line.split('|')
        winnings = set(winnings.split(':')[1].strip().split(' '))
        tries = tries.strip().split(' ')
        for t in tries:
            if t in winnings:
                if t.isnumeric():
                    count += 1
                    winnings.remove(t)
        print(count)
        result += count


    print(result)

