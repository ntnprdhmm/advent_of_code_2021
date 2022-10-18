input_file = open('5/input.txt', 'r')

lines = input_file.readlines()

counts = {}

for line in lines:
    start_coordinates, end_coordinates = line.strip().split(' -> ')
    start_x, start_y = [int(x) for x in start_coordinates.split(',')]
    end_x, end_y = [int(x) for x in end_coordinates.split(',')]

    if start_x == end_x:
        a, b = min(start_y, end_y), max(start_y, end_y)
        for i in range(a, b + 1):
            key = str(start_x) + ":" + str(i)
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
    elif start_y == end_y:
        a, b = min(start_x, end_x), max(start_x, end_x)
        for i in range(a, b + 1):
            key = str(i) + ":" + str(start_y)
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1

count = 0
for key in counts:
    if counts[key] > 1:
        count += 1

print(count)
