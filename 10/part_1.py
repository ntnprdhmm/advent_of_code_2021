from queue import LifoQueue

input_file = open('10/input.txt', 'r')

lines = input_file.readlines()

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}

def get__corrupted_char_if_any(line):
    q = LifoQueue()
    for c in line.strip():
        if c == '[' or c == '(' or c == '{' or c == '<':
            q.put(c)
        else:
            last_opening = q.get()
            if (last_opening == '[' and c != ']') or (last_opening == '(' and c != ')') or (last_opening == '{' and c != '}') or (last_opening == '<' and c != '>'):
                # print(last_opening, c)
                return c
    return None


result = 0

for line in lines:
    corrupted_char = get__corrupted_char_if_any(line)
    result += scores[corrupted_char]

print(result)