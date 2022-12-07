def visit_directory(f, directory,result):
     sum = 0
     for line in f:
          line = line.strip('\n').split(" ")
          if line[0] == "$" and line[1] == "cd" and line[2] != "..":
              sum += visit_directory(f,line[2],result)
          if line[0] == "$" and line[1] == "cd" and line[2] == "..":
              result.append(sum)
              return sum
          if line[0] != "$" and not line[0].isalpha():
               sum += int(line[0])
     result.append(sum)
     return sum
                       
with open('day7/input.txt') as f:
    result = []
    total_space = 70000000
    
    visit_directory(f, '',result)
    result.sort()
    unused_space = total_space - result[-1]
    for x in result:
        if x >= 30000000 - unused_space:
          print(x)
          break
        