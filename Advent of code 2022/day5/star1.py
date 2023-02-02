result = 0
with open('day5/input.txt') as f:
    stacks = []
    line_len = 0
    for line in f:
        if not stacks:
            line_len = len(line)
            stacks = [[] for i in range(line_len//4)]
        line = line.strip('\n')
        pos = 0
        if line_len == len(line) + 1:
            while pos < len(stacks):
                char = line[pos * 4 + 1]
                if char.isalpha():
                    stacks[pos].append(char)
                pos += 1 
        if len(line) == 0:
            for stack in stacks:
                stack.reverse()
        if line.startswith('m'):
            line = line.split(' ')

            number_of_move = int(line[1])
            start = int(line[3]) - 1
            end = int(line[5]) - 1
            while number_of_move:
                number_of_move -= 1
                crate = stacks[start].pop()
                stacks[end].append(crate)
    print(''.join([stack[-1] for stack in stacks]))
