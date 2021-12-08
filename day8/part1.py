import os
import numpy as np

# file1 = open(os.path.join(os.path.dirname(__file__), 'testinput.txt'), 'r')
file1 = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file1.readlines()


count = 0
for line in lines:
    segments, output = line.strip().split("|")

    print("segments:", segments)
    print("output:", output)

    for segment in output.strip().split(" "):
        print(segment)
        segment_length = len(segment)
        if (segment_length == 2 or segment_length == 3 or segment_length == 4 or segment_length == 7):
            count += 1

print(count)

# positions = list( map( int, lines[0].strip().split(",")))
