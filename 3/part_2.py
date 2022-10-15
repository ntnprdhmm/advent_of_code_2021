input_file = open('3/input.txt', 'r')

lines = input_file.readlines()

def sort_by_bit(lines, i):
    ones = []
    zeros = []
    for line in lines:
        if line[i] == "0":
            zeros.append(line)
        else:
            ones.append(line)
    return ones, zeros

oxygen_candidates = lines
oxygen_i = 0
while len(oxygen_candidates) > 1 and oxygen_i < len(lines[0]):
    ones, zeros = sort_by_bit(oxygen_candidates, oxygen_i)
    oxygen_candidates = ones if len(ones) >= len(zeros) else zeros
    oxygen_i += 1

co2_candidates = lines
co2_i = 0
while len(co2_candidates) > 1 and co2_i < len(lines[0]):
    ones, zeros = sort_by_bit(co2_candidates, co2_i)
    co2_candidates = ones if len(ones) < len(zeros) else zeros
    co2_i += 1

print(int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2))
