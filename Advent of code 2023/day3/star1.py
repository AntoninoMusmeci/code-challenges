def hasSymbol(i,j,input, nrow,ncolumn):
    
    for x,y in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        if 0 <= i + x < nrow and 0 <= j + y < ncolumn:
            print(i+x,j+y, ':',input[i + x][j + y])        
            if input[i + x][j + y] != '.' and  not input[i + x][j + y].isnumeric():
                return True
    return False

with open('input.txt') as f:
    input = []
    res = 0

    for line in f:
        input.append(line[:-1])
    for i in range(len(input)):
        number = ''
        symbol = False
        for j in range(len(input[0])):
            if input[i][j].isnumeric():

                number += input[i][j]
               
                if not symbol and hasSymbol(i,j,input,len(input),len(input[0])):
                    symbol = True
            else:
                if number != '':
                    if symbol:
                        number = int(number)
                        res += number
                number = ''
                symbol= False
        if number != '':
            if symbol:
                number = int(number)
                res += number
        number = ''
        symbol= False
            
    print(res)