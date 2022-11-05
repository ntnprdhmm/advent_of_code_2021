from queue import Queue

input_file = open('13/input.txt', 'r')

lines = input_file.readlines()

i = 0
points = []
while lines[i] != '\n':
    x, y = [int(v) for v in lines[i].strip().split(',')]
    points.append([x, y])
    i += 1

i += 1
instructions = []
while i < len(lines):
    fold_axe, line = lines[i].split(' ')[-1].split('=')
    instructions.append((fold_axe, int(line)))
    i += 1

def set_to_list(points):
    return [[int(v) for v in point.split(',')] for point in points]


def fold_y(y, points):
    surviving_points = set()
    for point in points:
        if point[1] > y:
            point[1] = y - (point[1] - y)
        surviving_points.add(str(point[0]) + ',' + str(point[1]))

    return set_to_list(surviving_points)


def fold_x(x, points):
    surviving_points = set()
    for point in points:
        if point[0] > x:
            point[0] = x - (point[0] - x)
        surviving_points.add(str(point[0]) + ',' + str(point[1]))

    return set_to_list(surviving_points)


surviving_points = None

for instruction in instructions:
    if instruction[0] == 'y':
        surviving_points = fold_y(instruction[1], points)
    else:
        surviving_points = fold_x(instruction[1], points)

def draw_points(points):
    max_x = 0
    max_y = 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    max_x += 1
    max_y += 1
    
    grid = [[' ']*max_x for i in range(max_y)]

    for point in points:
        grid[point[1]][point[0]] = '#'

    for line in grid:
        print(' '.join(line))

draw_points(surviving_points)