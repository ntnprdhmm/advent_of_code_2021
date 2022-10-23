from math import floor

input_file = open('7/input.txt', 'r')

lines = input_file.readlines()

crab_positions = [int(x) for x in lines[0].strip().split(',')]


def compute_triangle_number(n):
    return (n**2 + n) / 2


fuels_by_positions = [0] * max(crab_positions)

for position in range(len(fuels_by_positions)):
    for crab_position in crab_positions:
        steps = abs(crab_position - position)
        fuels = compute_triangle_number(steps)
        fuels_by_positions[position] += fuels

print(min(fuels_by_positions))
