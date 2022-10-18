input_file = open('6/input.txt', 'r')

lines = input_file.readlines()

ages = [int(x) for x in lines[0].strip().split(',')]

NUMBER_OF_DAYS = 80
NEW_BORN_DAYS_BEFORE_CREATING = 8


def init_lanternfishs_dict():
    d = {}
    for i in range(0, NEW_BORN_DAYS_BEFORE_CREATING + 1):
        d[i] = 0
    return d


lanternfishs = init_lanternfishs_dict()

for age in ages:
    if age in lanternfishs:
        lanternfishs[age] += 1
    else:
        lanternfishs[age] = 1

for _ in range(0, NUMBER_OF_DAYS):
    next_generation = init_lanternfishs_dict()

    # handle newborn lanternfishs
    next_generation[6] = lanternfishs[0]
    next_generation[8] = lanternfishs[0]
    lanternfishs[0] = 0

    # decrement days for others
    for i in range(1, NEW_BORN_DAYS_BEFORE_CREATING + 1):
        next_generation[i-1] += lanternfishs[i]

    lanternfishs = next_generation

total = 0
for i in range(0, NEW_BORN_DAYS_BEFORE_CREATING + 1):
    total += lanternfishs[i]
print(total)
