with open("day10/input.txt") as f:
    input = [l.split(" ") for l in f.read().splitlines()]
cycles = []
X = 1
p1 = 0
p2 = ""

current = input.pop(0)

next_current = False
cycle_count = 0

while len(input) > 0:
    pixel = len(cycles)

    if current[0] == "noop":
        if cycle_count == 1:
            next_current = True
    elif current[0] == "addx":
        if cycle_count == 2:
            X += int(current[1])
            next_current = True

    p2 += "#" if pixel % 40 in (X - 1, X, X + 1) else " "
    p2 += "\n" if pixel % 40 == 39 else ""

    if next_current:
        current = input.pop(0)
        next_current = False
        cycle_count = 0
    cycle_count += 1
    cycles.append(X)

for i in range(20, 221, 40):
    p1 += cycles[i - 1] * i

print(p1)
print(p2)