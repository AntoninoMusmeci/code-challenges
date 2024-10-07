def hasSymbol(i,j,input, nrow,ncolumn):
    gears = []
    for x,y in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        if 0 <= i + x < nrow and 0 <= j + y < ncolumn:
           
            if input[i + x][j + y] == '*':
                gears.append((i+x,j+y))
    return gears

with open('input.txt') as f:
    input = []
    res = {}
    tot = 0
    for line in f:
        input.append(line[:-1])
    for i in range(len(input)):
        number = ''
        symbol = False
        gears=[]
        for j in range(len(input[0])):
            if input[i][j].isnumeric():
                number += input[i][j]
                print(number)
                gears +=hasSymbol(i,j,input,len(input),len(input[0]))
            else:
                if number != '':
                    for gear in set(gears):
                        if gear not in res:
                            res[gear] = []
                        res[gear].append(int(number))
                number = ''
                symbol= False
                gears=[]
        if number != '':
            for gear in set(gears):
                if gear not in res:
                    res[gear] = []
                res[gear].append(int(number))
            number = ''
            symbol= False
            gears=[]
            
    for gear in res.values():
        print(gear)
        if len(gear) == 2:
            tot += gear[0] * gear[1]
    print(tot)