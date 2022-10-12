input_file = open('2/input.txt', 'r')

lines = input_file.readlines()

h = 0
d = 0
for line in lines:
    instruction, n_string = line.split(' ')
    n = int(n_string)

    if instruction == "forward":
        h += n
    elif instruction == "down":
        d += n
    else:
        d -= n 

print(h * d)
