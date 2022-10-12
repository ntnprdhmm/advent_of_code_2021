input_file = open('2/input.txt', 'r')

lines = input_file.readlines()

h = 0
d = 0
aim = 0
for line in lines:
    instruction, n_string = line.split(' ')
    n = int(n_string)

    if instruction == "down":
        aim += n
    elif instruction == "up":
        aim -= n        
    else:
        h += n
        d += aim * n

print(h * d)
