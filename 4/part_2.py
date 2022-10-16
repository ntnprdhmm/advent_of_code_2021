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


rows_cols = lines_to_boards_rows_cols(lines)

def compute_board_number(col):
    return col - (col % 10)

# transform to set so it's easier + more efficient
rows_cols = [set(x) for x in rows_cols]

# play the numbers on each rows and cols, until one is empty
def play_until_last_board_completed(numbers, rows_cols):
    number_of_boards = len(rows_cols) / 10

    finished_boards_start_indexes_set = set([])
    finished_boards_start_indexes = []

    for number in numbers:
        # apply the number on each rows and cols
        for i in range(0, len(rows_cols)):
            if number in rows_cols[i]:
                # remove it from the row or col if found
                rows_cols[i].remove(number)
                if len(rows_cols[i]) == 0:
                    # if the board has an empty row/col AND has not been marked as finished already
                    board_number = compute_board_number(i)
                    if not(board_number in finished_boards_start_indexes_set):
                        # mark it has finished
                        finished_boards_start_indexes_set.add(board_number)
                        finished_boards_start_indexes.append(board_number)
        # don't wait all numbers are played because it'll remove some numbers we need for the answer
        are_all_boards_finished = len(finished_boards_start_indexes) == number_of_boards
        if are_all_boards_finished:
            last = finished_boards_start_indexes[len(finished_boards_start_indexes) - 1]
            
            print(finished_boards_start_indexes)
            print(len(finished_boards_start_indexes))
            print(number_of_boards)
            return last, number, rows_cols 

    return -1, -1, -1


col, called_number, rows_cols = play_until_last_board_completed(numbers, rows_cols)
print("- col " , str(col))
print("- number " , str(called_number))

# sum the remaining values in the sets of this board
fs = 0
for i in range(col, col+5):
    fs += sum(rows_cols[i])

print(fs)
print(fs * called_number)

