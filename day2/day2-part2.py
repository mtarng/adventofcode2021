# file1 = open('/Users/mtarng/Workspace/adventofcode2021/day2/testinput.txt', 'r')
file1 = open('/Users/mtarng/Workspace/adventofcode2021/day2/input.txt', 'r')
lines = file1.readlines()

aim = 0
depth = 0
horizontal_distance = 0



count = 0
# last_val = int(lines[1])
for line in lines:

    direction, delta = line.split()

    if direction == "forward" :
        horizontal_distance += int(delta)
        depth += int(delta) * aim
    elif direction == "down" :
        aim += int(delta)
    elif direction == "up" :
        aim -= int(delta)

print("final depth: " + str(depth))
print("final distance: " + str(horizontal_distance))
print("multiplied: " + str(depth * horizontal_distance))