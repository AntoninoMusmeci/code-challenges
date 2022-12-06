import collections
with open('day6/input.txt') as f:
    line = f.readline()
    window_size = 4
    start = 0
    end = window_size
    while end <= len(line):
       window = collections.Counter(line[start:end])
       if len(window) == window_size:
            print(end)
            break 
       start += 1 
       end += 1


    
