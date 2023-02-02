import collections
total = 0
with open('day3/input.txt') as f:
    prev = ""
    k = 0
    for line in f:
        k += 1
        line = line.strip('\n')
        if prev == "":
            prev = line
            continue
        prev = set(prev).intersection(set(line))
        if k == 3:
            k = 0
            value = prev.pop()
            prev = ""
            if value.isupper():
                total += 26 + ((ord(value) - ord('A')) + 1)
            else:
                total += (ord(value) - ord('a')) + 1
    print(total)
       