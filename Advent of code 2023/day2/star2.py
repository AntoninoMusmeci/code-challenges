with open('input.txt') as f:
    tot = {'r':0, 'g':0, 'b':0}
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
                tot[color] = max(number, tot[color])
        print(tot)
        res += tot['r'] * tot['g'] * tot['b']
        tot = {'r':0, 'g':0, 'b':0}
    print(res)
        