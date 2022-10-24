input_file = open('9/input.txt', 'r')

lines = input_file.readlines()

grid = []
for j in range(len(lines)):
    line = lines[j].strip()
    grid_line = []
    for i in range(len(line)):
        grid_line.append(int(line[i]))
    grid.append(grid_line)

result = 0

for j in range(len(grid)):
    for i in range(len(grid[j])):
        top = j == 0 or grid[j-1][i] > grid[j][i]
        bottom = (j == (len(grid) - 1)) or grid[j+1][i] > grid[j][i]
        left = i == 0 or grid[j][i-1] > grid[j][i] 
        right = (i == (len(grid[j]) - 1)) or grid[j][i+1] > grid[j][i]

        if (top and bottom and left and right):
            result += 1 + grid[j][i]

print(result)
