import os
import numpy as np

# file1 = open(os.path.join(os.path.dirname(__file__), 'testinput.txt'), 'r')
file1 = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file1.readlines()


fishes = list( map( int, lines[0].strip().split(",")))

for day in range (80):
    print("after day", day + 1)
    print(fishes)

    new_fishes_count = 0

    for fish_index in range(len(fishes)):
        if fishes[fish_index] == 0:
            fishes[fish_index] = 6
            new_fishes_count += 1
        else:
            fishes[fish_index] = fishes[fish_index] - 1
    
    for i in range(new_fishes_count):
        fishes.append(8)


print(len(fishes))