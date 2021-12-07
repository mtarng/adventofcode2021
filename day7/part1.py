import os
import numpy as np

# file1 = open(os.path.join(os.path.dirname(__file__), 'testinput.txt'), 'r')
file1 = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file1.readlines()


positions = list( map( int, lines[0].strip().split(",")))

print(positions)

total = sum(positions)
num = len(positions)
avg = total/num
print("total:", total)
print("num:", num)
print("avg:", avg)

max = max(positions)
print("max:", max)
min = min(positions)
print("min:", min)
range = range(min, max + 1)
print("range:", range)

print()

min_index = min
min_fuel = max * num
for index in range:
    print("index:", index)
    crab_fuel_needed = list( map( lambda p: abs( index - p), positions))
    print(crab_fuel_needed)


    print(sum(crab_fuel_needed))
    if min_fuel > sum(crab_fuel_needed):
        min_fuel = sum(crab_fuel_needed)
    
print("min_fuel", min_fuel)
