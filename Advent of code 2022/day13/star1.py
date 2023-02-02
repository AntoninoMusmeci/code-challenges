

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
    for i, block in enumerate(input.split("\n\n")):
        left, right = block.splitlines()
        print(left)
        left1, right = eval(left), eval(right)
        if compare(left, right) == -1:
            total += i + 1
    print(total)
