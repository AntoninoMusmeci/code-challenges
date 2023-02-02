

f = open('day15/input.txt').readlines()
data = [line.strip("\n") for line in f]
pairs = [tuple(map(lambda item: tuple(map(lambda x: int(x[2:]), item.replace(",", "").split()[-2:])), line.split(": "))) for line in data]
target = 10 if pairs[0] == ((2, 18), (-2, 15)) else 2000000
x_ranges = []
for pair in pairs:
    distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
    dx = distance - abs(target - pair[0][1])
    if dx >= 0:
        x_ranges.append((pair[0][0] - dx, pair[0][0] + dx))

x_ranges.sort()

map = x_ranges[0]
void = []
for i in range(1, len(x_ranges)):
    if x_ranges[i][0] <= map[1]:
        map = (map[0], max(map[1], x_ranges[i][1]))
    else:
        void.extend(list(range(map[1] + 1, x_ranges[i][0])))

num_sensors = len(set([i[0] for i in pairs if i[0][1] == target and map[0] <= i[0][0] <= map[1]]))
num_beacons = len(set([i[1] for i in pairs if i[1][1] == target and map[0] <= i[1][0] <= map[1]]))

print (map[1] - map[0] + 1) - num_sensors - num_beacons - len(void)




