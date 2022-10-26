from queue import Queue

input_file = open('11/input.txt', 'r')

lines = input_file.readlines()

grid = []
for line in lines:
    grid.append([int(x) for x in line.strip()])

flashes = 0

d = 0

def to_key(i, j):
    return str(i) + ':' + str(j)

def display_grid(grid):
    for line in grid:
        print(''.join([str(v) for v in line]))
    print('')

for _ in range(100):
    flashed = set()
    q = Queue()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                q.put((i, j))
                flashes += 1
                flashed.add(to_key(i, j))
    
    while not q.empty():
        e = q.get()
        i, j = e[0], e[1]

        len_row = len(grid[i]) - 1
        len_col = len(grid) - 1

        # top
        k_top = to_key(i-1, j)
        if i > 0 and k_top not in flashed:
            grid[i-1][j] += 1
            if grid[i-1][j] > 9:
                flashed.add(k_top)
                flashes += 1

        # top left
        k_top_left = to_key(i-1, j-1)
        if i > 0 and j > 0 and k_top_left not in flashed:
            grid[i-1][j-1] += 1
            if grid[i-1][j-1] > 9:
                flashed.add(k_top_left)
                flashes += 1
        
        # top right
        k_top_right = to_key(i-1, j+1)
        if i > 0 and j < len_row and k_top_right not in flashed:
            grid[i-1][j+1] += 1
            if grid[i-1][j+1] > 9:
                flashed.add(k_top_right)
                flashes += 1
        
        # middle left
        k_middle_left = to_key(i, j-1)
        if j > 0 and k_middle_left not in flashed:
            grid[i][j-1] += 1
            if grid[i][j-1] > 9:
                flashed.add(k_middle_left)
                flashes += 1

        # middle right
        k_middle_right = to_key(i, j+1)
        if j < len_row and k_middle_right not in flashed:
            grid[i][j+1] += 1
            if grid[i][j+1] > 9:
                flashed.add(k_middle_right)
                flashes += 1
        
        # bot
        k_bot = to_key(i+1, j)
        if i < len_col and k_bot not in flashed:
            grid[i+1][j] += 1
            if grid[i+1][j] > 9:
                flashed.add(k_bot)
                flashes += 1

        # bot left
        k_bot_left = to_key(i+1, j-1)
        if i < len_col and j > 0 and k_bot_left not in flashed:
            grid[i+1][j-1] += 1
            if grid[i+1][j-1] > 9:
                flashed.add(k_bot_left)
                flashes += 1
        
        # bot right
        k_top_right = to_key(i+1, j+1)
        if i < len_col and j < len_row and k_top_right not in flashed:
            grid[i+1][j+1] += 1
            if grid[i+1][j+1] > 9:
                flashed.add(k_top_right)
                flashes += 1

    for e in flashed:
        i, j = [int(v) for v in e.split(':')]
        grid[i][j] = 0

    if d < 10:
        display_grid(grid)
        d += 1


print(flashes)
