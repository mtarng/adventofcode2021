# file1 = open('/Users/mtarng/Workspace/adventofcode2021/day3/testinput.txt', 'r')
file1 = open('/Users/mtarng/Workspace/adventofcode2021/day3/input.txt', 'r')
lines = file1.readlines()

num_bits = len(lines[0].strip())
bit_counts = [0] * num_bits

index = 0
for line in lines:

    # for each character, check if 0 or 1
    for i in range(num_bits):
        if line[i] == "0":
            # print("zero!")
            bit_counts[i] -= 1
        else:
            # print("one!")
            bit_counts[i] += 1

print(bit_counts)

gamma_str = ""
epislon_str = ""
for b in bit_counts:
    if b > 0:
        gamma_str += "1"
        epislon_str += "0"
    else :
        gamma_str += "0"
        epislon_str += "1"


print(gamma_str)
print(epislon_str)


gamma_rate = int(gamma_str, 2)
episilon_rate = int(epislon_str, 2)

print("gamma rate: " + str(gamma_rate))
print("epsilon rate: " + str(episilon_rate))
print("multiplied: " + str(gamma_rate * episilon_rate))