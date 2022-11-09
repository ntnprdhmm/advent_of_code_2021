import sys
import heapq
from math import floor

input_file = open('15/input.txt', 'r')
lines = [s.strip() for s in input_file.readlines()]

GRID_REPEAT = 5
GRID_ROWS = len(lines)
GRID_COLS = len(lines[0])
max_y = (GRID_ROWS * GRID_REPEAT) - 1
max_x = (GRID_COLS * GRID_REPEAT) - 1

# risk for each tuple (x,y)
coords_risks = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        coords_risks[(x, y)] = int(c)

def compute_risk(coord):
    x, y = coord
    risk_inc = 0

    while x > (GRID_COLS - 1):
        x = x - GRID_COLS
        risk_inc += 1

    while y > (GRID_ROWS - 1):
        y = y - GRID_ROWS
        risk_inc += 1
    
    risk = coords_risks[(x, y)] + risk_inc

    if risk > 9:
        risk %= 9
    return risk

start = (0, 0)
less_risk_from_start = {start: 0}  # risk from start to start is 0
visited = set()
prev = {}

queue = []
heapq.heappush(queue, (0, start))

while len(queue):
    current_risk, current = heapq.heappop(queue)

    # mark as visited
    visited.add(current)

    # if already a lower risk to this node, skip
    if less_risk_from_start[current] < current_risk:
        continue

    # find neighbors
    x, y = current
    # all
    neighbors = [(x+dx, y+dy) for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]]
    # filter out neighbors outside boundaries
    neighbors = [(x, y) for x, y in neighbors if x >= 0 and x <= max_x and y >= 0 and y <= max_y]
    # filter out already visited neighbors
    neighbors = [neighbor for neighbor in neighbors if neighbor not in visited]

    for neighbor in neighbors:
        new_risk = less_risk_from_start[current] + compute_risk(neighbor)

        # if risk lower than the risk in less_risk_from_start, set it
        if (neighbor not in less_risk_from_start) or new_risk < less_risk_from_start[neighbor]:
            less_risk_from_start[neighbor] = new_risk
            # lower risk to neighbor is from current, remember it
            prev[neighbor] = current
            # queue the neighbor
            heapq.heappush(queue, (new_risk, neighbor))

print(less_risk_from_start[(max_x, max_y)])
