input_file = open('1/input.txt', 'r')

lines = input_file.readlines()

n = 0
for i in range(1, (len(lines))):
    if int(lines[i]) > int(lines[i-1]):
        n += 1

print(n)
