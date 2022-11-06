from math import ceil

input_file = open('14/input.txt', 'r')

lines = input_file.readlines()

template = lines[0].strip()

rules = {}
for i in range(2, len(lines)):
    adjacents, to_insert = lines[i].strip().split(' -> ')
    rules[adjacents] = to_insert

steps = 40

pairs = {}
chars_counts = {}

for i in range(len(template)-1):
    pair = template[i]+template[i+1]
    if pair not in pairs:
        pairs[pair] = 0
    pairs[pair] += 1
for c in template:
    if c not in chars_counts:
        chars_counts[c] = 0
    chars_counts[c] += 1

print(chars_counts)

for _ in range(steps):
    pairs_after_step = {}

    for pair in pairs:
        count = pairs[pair]
        rule = rules[pair]
        p1 = pair[0] + rule
        p2 = rule + pair[1]

        if p1 not in pairs_after_step:
            pairs_after_step[p1] = 0
        if p2 not in pairs_after_step:
            pairs_after_step[p2] = 0

        pairs_after_step[p1] += count
        pairs_after_step[p2] += count
        if rule not in chars_counts:
            chars_counts[rule] = 0
        chars_counts[rule] += count

    pairs = pairs_after_step

print(chars_counts)

max_count = 0
min_count = 100000000000000

for count in chars_counts:
    if chars_counts[count] < min_count:
        min_count = chars_counts[count]
    if chars_counts[count] > max_count:
        max_count = chars_counts[count]

print(max_count)
print(min_count)
print(max_count - min_count)
