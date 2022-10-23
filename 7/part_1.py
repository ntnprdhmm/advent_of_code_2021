from math import floor

input_file = open('7/input.txt', 'r')

lines = input_file.readlines()

positions = [int(x) for x in lines[0].strip().split(',')]

positions.sort()

def get_median_position(positions):
    n = len(positions)
    if len(positions) % 2:
        return (positions[n] + positions[n-1]) / 2
    return positions[floor(n / 2)]

median = get_median_position(positions)
print(median)

diffs = [abs(p - median) for p in positions]

print(sum(diffs))