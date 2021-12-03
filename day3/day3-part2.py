# file1 = open('/Users/mtarng/Workspace/adventofcode2021/day3/testinput.txt', 'r')
file1 = open('/Users/mtarng/Workspace/adventofcode2021/day3/input.txt', 'r')
lines = file1.readlines()

num_bits = len(lines[0].strip())

# Oxygen - keep most common bit value - 1 if equal
lines_for_analysis = lines
index = 0
while len(lines_for_analysis) > 1:
    lines_kept = []
    bit_count = 0
    for line in lines_for_analysis:
        if line[index] == "0":
            # print("zero!")
            bit_count -= 1
        else:
            # print("one!")
            bit_count += 1
    
    # remove lines with wrong value?
    print (bit_count)
    if bit_count >= 0:
        # keep all lines with 1 at index
        for line in lines_for_analysis:
            if line[index] == "1":
                lines_kept.append(line)
    else :
        # keep all lines with 0 at index
        for line in lines_for_analysis:
            if line[index] == "0":
                lines_kept.append(line)
    lines_for_analysis = lines_kept
    index += 1

oxygen_str = lines_for_analysis[0]
print("oxygen result: " + oxygen_str)

# CO2 - keep least common bit value - 0 if equal
lines_for_analysis = lines
index = 0
while len(lines_for_analysis) > 1:
    lines_kept = []
    bit_count = 0
    for line in lines_for_analysis:
        if line[index] == "0":
            # print("zero!")
            bit_count -= 1
        else:
            # print("one!")
            bit_count += 1
    
    # remove lines with wrong value?
    print (bit_count)
    if bit_count < 0:
        for line in lines_for_analysis:
            if line[index] == "1":
                lines_kept.append(line)
    else :
        # keep all lines with 0 at index
        for line in lines_for_analysis:
            if line[index] == "0":
                lines_kept.append(line)
    lines_for_analysis = lines_kept
    index += 1

co2_str = lines_for_analysis[0]
print("co2 result: " + co2_str)


print(oxygen_str)
print(co2_str)


oxygen_rate = int(oxygen_str, 2)
co2_rate = int(co2_str, 2)

print("oxygen rate: " + str(oxygen_rate))
print("co2 rate: " + str(co2_rate))
print("multiplied: " + str(oxygen_rate * co2_rate))