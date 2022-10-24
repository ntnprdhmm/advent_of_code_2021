from queue import Queue

input_file = open('9/input.txt', 'r')

lines = input_file.readlines()

EMPTY = ' '
FULL = 'X'


def display_grid(grid):
    for line in grid:
        print(' '.join([str(v) for v in line]))


grid = []
for j in range(len(lines)):
    line = lines[j].strip()
    grid_line = []
    for i in range(len(line)):
        v = int(line[i])
        grid_line.append(EMPTY if v < 9 else FULL)
    grid.append(grid_line)

# display_grid(grid)

already_processed_emtpy_cells = set()


def explore_empty_area(grid, start_i, start_j):
    q = Queue()
    q.put([start_i, start_j])
    
    key = str(start_j) + ':' + str(start_i)
    already_processed_emtpy_cells.add(key)

    size = 0
    while not q.empty():
        e = q.get()
        print(e)
        [i, j] = e

        size += 1

        if j > 0 and grid[j-1][i] == EMPTY:
            ktop = str(j-1) + ':' + str(i)
            if ktop not in already_processed_emtpy_cells:
                already_processed_emtpy_cells.add(ktop)
                q.put([i, j-1])

        if j < (len(grid)-1) and grid[j+1][i] == EMPTY:
            kbot = str(j+1) + ':' + str(i)
            if kbot not in already_processed_emtpy_cells:
                already_processed_emtpy_cells.add(kbot)
                q.put([i, j+1])

        if i > 0 and grid[j][i-1] == EMPTY:
            kleft = str(j) + ':' + str(i-1)
            if kleft not in already_processed_emtpy_cells:
                already_processed_emtpy_cells.add(kleft)
                q.put([i-1, j])

        if i < (len(grid[j])-1) and grid[j][i+1] == EMPTY:
            kright = str(j) + ':' + str(i+1)
            if kright not in already_processed_emtpy_cells:
                already_processed_emtpy_cells.add(kright)
                q.put([i+1, j])
    
    print("_______")

    return size


empty_area_sizes = []
for j in range(len(grid)):
    for i in range(len(grid[j])):
        key = str(j) + ':' + str(i)
        if grid[j][i] == EMPTY and key not in already_processed_emtpy_cells:
            # discovered a new empty area -> compute his size !
            size = explore_empty_area(grid, i, j)
            empty_area_sizes.append(size)

empty_area_sizes.sort(reverse=True)
print(empty_area_sizes[0] * empty_area_sizes[1] * empty_area_sizes[2])
