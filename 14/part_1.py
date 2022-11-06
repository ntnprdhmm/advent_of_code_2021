from queue import Queue

input_file = open('14/input.txt', 'r')

lines = input_file.readlines()

template = lines[0].strip()

rules = {}
for i in range(2, len(lines)):
    adjacents, to_insert = lines[i].strip().split(' -> ')
    rules[adjacents] = to_insert

steps = 10

polymer = template

for _ in range(steps):
    inserts = []
    for i in range(0, len(polymer) - 1):
        pair = polymer[i] + polymer[i+1]
        inserts.append(rules[pair])
    
    next_polymer = ''
    for i in range(len(inserts)):
        next_polymer += polymer[i] + inserts[i]
    polymer = next_polymer + polymer[-1]

def count_occurences(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

min_occurences = len(polymer)
max_occurences = 0

d = count_occurences(polymer)

for c in d:
    if d[c] < min_occurences:
        min_occurences = d[c]
    if d[c] > max_occurences:
        max_occurences = d[c]

print(max_occurences - min_occurences)
