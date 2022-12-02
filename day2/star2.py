max_calories = 0
total = 0
with open('day2/input.txt') as f:
    for line in f:
        line = line.strip('\n').split()
        opponent_move =  ord(line[0]) - ord("A")      
        result = ord(line[1]) - ord("X") 
        total += result * 3
        if result == 0: total += (opponent_move + 2) %3 + 1
        if result == 1: total += opponent_move + 1
        if result == 2: total += (opponent_move + 1) %3 + 1
    print(total)
       