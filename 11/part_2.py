from queue import Queue

input_file = open('11/input.txt', 'r')

lines = input_file.readlines()

grid = []
for line in lines:
    grid.append([int(x) for x in line.strip()])

def to_key(i, j):
    return str(i) + ':' + str(j)

def display_grid(grid):
    for line in grid:
        print(line)
    print('')

nb_octopuses = len(grid) * len(grid[0])

all_flashed = -1
step = 1
while all_flashed == -1:
    to_flash = Queue()
    flashed = set()

    # increase energy level of each octopus
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                to_flash.put((i, j))
                flashed.add(to_key(i, j))

    while not to_flash.empty():
        # flash

        octopus = to_flash.get()
        i, j = octopus[0], octopus[1]
        flashed.add(to_key(i, j))

        len_row = len(grid[i]) - 1
        len_col = len(grid) - 1

        if i > 0:
            grid[i-1][j] += 1

        if i > 0 and j > 0:
            grid[i-1][j-1] += 1
        
        if i > 0 and j < len_row:
            grid[i-1][j+1] += 1
        
        if j > 0:
            grid[i][j-1] += 1

        if j < len_row:
            grid[i][j+1] += 1
        
        if i < len_col:
            grid[i+1][j] += 1

        if i < len_col and j > 0:
            grid[i+1][j-1] += 1
        
        if i < len_col and j < len_row:
            grid[i+1][j+1] += 1

        # queue next octopuses to flash
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                k = to_key(x, y)
                if k not in flashed and grid[x][y] > 9:
                    to_flash.put((x, y))
                    flashed.add(k)

    # set flashed octopuses to 0

    if nb_octopuses == len(flashed):
        all_flashed = step
    step += 1

    for octopus in flashed:
        i, j = [int(v) for v in octopus.split(':')]
        grid[i][j] = 0


print(all_flashed)
