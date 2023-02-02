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
    size_sum = 0
    visit_directory(f, '',result)
    print(result)
    for x in result:
        if x <= 100000:
          size_sum += x
    print(size_sum)
        