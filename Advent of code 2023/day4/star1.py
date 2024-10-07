with open('input.txt') as f:

    result = 0
    for i,line in enumerate(f):
        count = 0
        if '\n' in line:
            line = line[:-1]
        [winnings, tries] = line.split('|')
        winnings = set(winnings.split(':')[1].strip().split(' '))
        tries = tries.strip().split(' ')



        print(tries,winnings)
        for t in tries:
            if t in winnings:
                if t.isnumeric():
                    count += 1
                    winnings.remove(t)
      
        if count:
            result += 2**(count - 1)


    print(result)


        