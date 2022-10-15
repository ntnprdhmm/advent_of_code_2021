input_file = open('3/input.txt', 'r')

lines = input_file.readlines()

counts_1 = [0] * len(lines[0].strip())

for i in range(0, len(lines)):
    line = lines[i]
    for j in range(0, len(line)):
        if line[j] == "1":
            counts_1[j] += 1

a, b = "", ""

for j in range(0, len(counts_1)):
    if counts_1[j] > (len(lines) - counts_1[j]):
        a += "1"
        b += "0"
    else:
        a += "0"
        b += "1"

print(int(a, 2) * int (b, 2))
