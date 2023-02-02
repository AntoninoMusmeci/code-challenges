
f = open('day15/input.txt').readlines()
data = [line.strip("\n") for line in f]
temps = [tuple(map(lambda item: tuple(map(lambda x: int(x[2:]), item.replace(",", "").split()[-2:])), line.split(": "))) for line in data]
pairs = [(sensor, beacon, abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])) for sensor, beacon in temps]
targets = 20 if pairs[0] == ((2, 18), (-2, 15)) else 4000000

for target in range(targets + 1):
    x_ranges = []
    for sensor, _, distance in pairs:
        dx = distance - abs(target - sensor[1])
        if dx >= 0:
            x_ranges.append((sensor[0] - dx, sensor[0] + dx))
    x_ranges.sort()
    map = x_ranges[0]
    for i in range(1, len(x_ranges)):
        if map[1] > x_ranges[i][0]:
            map = (map[0], max(map[1], x_ranges[i][1]))
        else:
            print((map[1] + 1) * 4000000 + target)
            break