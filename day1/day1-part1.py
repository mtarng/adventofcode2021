# file1 = open('/Users/mtarng/Workspace/adventofcode2021/day1/testinput.txt', 'r')
file1 = open('/Users/mtarng/Workspace/adventofcode2021/day1/input.txt', 'r')
Lines = file1.readlines()


count = 0
last_val = int(Lines[1])
for line in Lines:
    val = int(line)
    if last_val < val:
        count += 1
    last_val = val

print(count)