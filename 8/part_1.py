input_file = open('8/input.txt', 'r')

lines = input_file.readlines()

count_1_4_7_8 = 0

for line in lines:
    output_values = line.split(' | ')[1].strip().split(' ')
    for value in output_values:
        if len(value) in [2, 3, 4, 7]:
            count_1_4_7_8 += 1

print(count_1_4_7_8)