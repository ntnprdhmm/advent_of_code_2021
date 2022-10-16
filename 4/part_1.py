input_file = open('4/input.txt', 'r')

lines = input_file.readlines()

numbers = [int(x) for x in lines[0].split(',')]

def lines_to_boards_rows_cols(lines):
    # 5 raws 5 cols, for each boards
    rows_cols = []

    j = 6
    for i in range(1, len(lines)):
        if j == 6:
            j -= 1
            continue

        rows_cols.append([int(x)
                         for x in lines[i].strip().split(' ') if x != ''])

        j -= 1

        if j == 0:
            j = 6

            # create the cols from the 5 prevous rows
            for a in range(0, 5):
                rows_cols.append([
                    rows_cols[len(rows_cols) - (5+a)][a],
                    rows_cols[len(rows_cols) - (4+a)][a],
                    rows_cols[len(rows_cols) - (3+a)][a],
                    rows_cols[len(rows_cols) - (2+a)][a],
                    rows_cols[len(rows_cols) - (1+a)][a],
                ])

    return rows_cols


def debug_rows_col(rows_cols):
    for i in range(0, len(rows_cols), 10):
        print("---- BOARD " + str(i))
        print("rows")
        print(' '.join([str(x) for x in rows_cols[i]]))
        print(' '.join([str(x) for x in rows_cols[i+1]]))
        print(' '.join([str(x) for x in rows_cols[i+2]]))
        print(' '.join([str(x) for x in rows_cols[i+3]]))
        print(' '.join([str(x) for x in rows_cols[i+4]]))
        print("cols")
        print(' '.join([str(x) for x in rows_cols[i+5]]))
        print(' '.join([str(x) for x in rows_cols[i+6]]))
        print(' '.join([str(x) for x in rows_cols[i+7]]))
        print(' '.join([str(x) for x in rows_cols[i+8]]))
        print(' '.join([str(x) for x in rows_cols[i+9]]))
        print("")


rows_cols = lines_to_boards_rows_cols(lines)
debug_rows_col(rows_cols)

# transform to set so it's easier + more efficient
rows_cols = [set(x) for x in rows_cols]

# play the numbers on each rows and cols, until one is empty
def play(numbers, rows_cols):
    for number in numbers:
        first_winner_board = -1
        for i in range(0, len(rows_cols)):
            if number in rows_cols[i]:
                rows_cols[i].remove(number)
                if len(rows_cols[i]) == 0:
                    if first_winner_board == -1:
                        first_winner_board = i
        if first_winner_board != -1:
            return first_winner_board, number, rows_cols

    return -1, -1, -1


col, called_number, rows_cols = play(numbers, rows_cols)
print("- col " , str(col))
print("- number " , str(called_number))

# find the start of the board in rows_cols
start_index = col - (col % 10)
print(start_index)

# sum the remaining values in the sets of this board
fs = 0
for i in range(start_index, start_index+5):
    fs += sum(rows_cols[i])

print(fs)
print(fs * called_number)

