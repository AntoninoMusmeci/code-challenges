
import sys
from Point import Point


f = open('day14/input.txt')
data = f.read().strip()
blocked = set()

for line in data.splitlines():
    parts = [Point(*map(int, part.split(","))) for part in line.split(" -> ")]
    for i in range(len(parts) - 1):
        start, end = parts[i], parts[i + 1]

        if start.x == end.x:
            for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
                blocked.add(Point(start.x, y))
        else:
            for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
                blocked.add(Point(x, start.y))

steps = 0
while True:
    sand = Point(500, 0)

    for _ in range(1000):
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            next_point = sand.add(dx, dy)
            if next_point not in blocked:
                sand = next_point
                break
        else:
            break
    else:
        print(steps)
        break

    blocked.add(sand)
    steps += 1

