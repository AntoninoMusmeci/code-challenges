


digits = [('one',1), ('two',2), ('three',3), ('four',4), ('five',5), ('six',6), ('seven', 7), ('eight',8), ('nine',9),('1',1),('2',2),
          ('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9)]


with open('input.txt') as f:
    tot = 0
    for line in f:
        l = 0
        r = len(line) - 1
        currentFirst = 10000000
        currentLast = -1
        number = [None,None]
        for digit in digits:
            first = line.find(digit[0])
            if first != -1 and first <= currentFirst:
                currentFirst = first
                number[0] = digit[1]
            last = line.rfind(digit[0])
            if last != -1 and last > currentLast:
                currentLast = last
                number[1] = digit[1]
        tot += number[0] * 10 + number[1]
    print(tot)