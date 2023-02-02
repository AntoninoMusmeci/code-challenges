import collections
total = 0
with open('day3/input.txt') as f:
    for line in f:
        line = line.strip('\n')
        rucksack_len = len(line)
        compartment1 = set(line[0:rucksack_len//2])
        compartment2 = set(line[rucksack_len//2:rucksack_len])
        value = compartment1.intersection(compartment2).pop()
        if value.isupper():
            total += 26 + ((ord(value) - ord('A')) + 1)
        else:
            total += (ord(value) - ord('a')) + 1
        
    print(total)
       