with open('input.txt') as f:
    tot = {'r':12, 'g':13, 'b':14}
    res = 0
    for i,line in enumerate(f):
        input = line.split(': ')[1]
        input = input.split('; ')
        possible = True
        for round in input:
            cubes = round.split(', ')
            for cube in cubes:
                number = int(cube.split(' ')[0])
                color = cube.split(' ')[1][0]
                if number > tot[color[0]]:
                    print(number, '>', color , tot[color[0]])
                    possible = False
        
        if possible:
            res += i + 1
        else:
            print('Game:', i + 1, 'impossible')
        
    print(res)
        