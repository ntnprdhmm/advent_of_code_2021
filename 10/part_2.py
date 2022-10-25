from queue import LifoQueue

input_file = open('10/input.txt', 'r')

lines = input_file.readlines()

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    None: 0
}


def get_missing_chars_if_not_corrupted(line):
    q = LifoQueue()
    for c in line.strip():
        if c == '[' or c == '(' or c == '{' or c == '<':
            q.put(c)
        else:
            last_opening = q.get()
            if (last_opening == '[' and c != ']') or (last_opening == '(' and c != ')') or (last_opening == '{' and c != '}') or (last_opening == '<' and c != '>'):
                return ''

    missing_chars = ''

    while not q.empty():
        c = q.get()
        if c == '(':
            missing_chars += ')'
        elif c == '[':
            missing_chars += ']'
        elif c == '{':
            missing_chars += '}'
        else:
            missing_chars += '>'

    return missing_chars


results = []

for line in lines:
    chars = get_missing_chars_if_not_corrupted(line)
    result = 0
    for c in chars:
        result = (5 * result) + scores[c]
    if result != 0:
        results.append(result)

results.sort()

print(results)
print(results[int((len(results) - 1) / 2)])
