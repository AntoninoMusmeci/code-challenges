
from functools import cmp_to_key
def compare(left, right):
    if type(left) != list:
        left = [left]
    if type(right) != list:
        right = [right]
    for i in range(min(len(left), len(right))):
        if type(left[i]) == list or type(right[i]) == list:
            result = compare(left[i], right[i])
            if result:
                return result
        elif left[i] < right[i]:
            return -1
        elif left[i] > right[i]:
            return 1

    if len(left) < len(right):
        return -1

    if len(left) > len(right):
        return 1
    return 0


with open('day13/input.txt') as f:
    input = f.read().strip()
    total = 0
    packets = []
    for block in input.split("\n\n"):
        left, right = block.splitlines()
        left, right = eval(left), eval(right)

        packets.append(left)
        packets.append(right)

    divider1 = [[2]]
    divider2 = [[6]]
    packets.extend([divider1, divider2])
    packets = sorted(packets, key=cmp_to_key(compare))
    print((packets.index(divider1) + 1) * (packets.index(divider2) + 1))
