total = 0
with open('day2/input.txt') as f:
    for line in f:
        line = line.strip('\n').split()
        opponent_move =  ord(line[0]) - ord("A")      
        my_move = ord(line[1]) - ord("X") 
        total += my_move + 1
        if (opponent_move + 1) %3 == my_move: 
            total += 6
        if opponent_move == my_move: 
            total += 3
    print(total)
       