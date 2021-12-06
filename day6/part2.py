import os
import numpy as np

# file1 = open(os.path.join(os.path.dirname(__file__), 'testinput.txt'), 'r')
file1 = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file1.readlines()


fishes_input = list( map( int, lines[0].strip().split(",")))


fishes = [0] * 9

for fish in fishes_input:
    fishes[fish] += 1

print(fishes)

for day in range (256):
    print("after day", day + 1, ": ", fishes)

    new_fishes = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7] + new_fishes
    fishes[7] = fishes[8] 
    fishes[8] = new_fishes


print(sum(fishes))


# for day in range (256):
#     print("after day", day + 1)
#     # print(fishes)

#     new_fishes_count = 0

#     for fish_index in range(len(fishes)):
#         if fishes[fish_index] == 0:
#             fishes[fish_index] = 6
#             new_fishes_count += 1
#         else:
#             fishes[fish_index] = fishes[fish_index] - 1
    
#     for i in range(new_fishes_count):
#         fishes.append(8)


# print(len(fishes))