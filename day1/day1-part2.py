# file1 = open('/Users/mtarng/Workspace/adventofcode2021/day1/testinput.txt', 'r')
file1 = open('/Users/mtarng/Workspace/adventofcode2021/day1/input.txt', 'r')
Lines = file1.readlines()

scan_groups = []
for i in range(len(Lines) - 2):
    sum = int(Lines[i]) + int(Lines[i+1]) + int(Lines[i+2])
    scan_groups.append(sum)
# print(scan_groups)


count = 0
last_val = int(scan_groups[1])
for group in scan_groups:
    val = int(group)
    if last_val < val:
        count += 1
    last_val = val

print(count)