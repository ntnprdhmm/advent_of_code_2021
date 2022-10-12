input_file = open('1/input.txt', 'r')

lines = input_file.readlines()

n = 0
for i in range(3, (len(lines))):
    a = int(lines[i-3]) + int(lines[i-2]) + int(lines[i-1])
    b = int(lines[i-2]) + int(lines[i-1]) + int(lines[i])
    if b > a:
        n += 1

print(n)
