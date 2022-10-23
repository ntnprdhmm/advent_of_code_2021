input_file = open('8/input.txt', 'r')

lines = input_file.readlines()

# indexes for the segments
#
#  |--0--|
#  5     1
#  |--6--|
#  4     2
#  |--3--|

TOP = 0
TOP_RIGHT = 1
BOTTOM_RIGHT = 2
BOTTOM = 3
BOTTOM_LEFT = 4
TOP_LEFT = 5
MIDDLE = 6


def find_by_length(a, l):
    for v in a:
        if len(v) == l:
            return v
    return None


def check_if_using_only_one_value_of_each_sets(candidate, sets):
    for s in sets:
        count = 0
        for c in candidate:
            if c in s:
                count += 1
        if count != 1:
            return False

    return True


def find_signal_of_length_using_only_one_value_of_each_sets(signal_patterns, l, sets):
    candidates = []
    for s in signal_patterns:
        if len(s) == l:
            candidates.append(s)
    for candidate in candidates:
        if check_if_using_only_one_value_of_each_sets(candidate, sets):
            return candidate

    return None


def map_signal_patterns(signal_patterns):
    segments = [set([])] * 7

    # process unique length signals

    signal_one, signal_four, signal_seven, signal_eight = find_by_length(signal_patterns, 2), find_by_length(
        signal_patterns, 4), find_by_length(signal_patterns, 3), find_by_length(signal_patterns, 7)

    segments[TOP_RIGHT] = set(signal_one)
    segments[BOTTOM_RIGHT] = segments[TOP_RIGHT]

    segments[TOP] = set(signal_seven) - segments[TOP_RIGHT]

    segments[MIDDLE] = set(
        signal_four) - segments[TOP_RIGHT]
    segments[TOP_LEFT] = segments[MIDDLE]

    segments[BOTTOM] = (
        (set(signal_eight) - segments[TOP_RIGHT]) - segments[TOP_LEFT]) - segments[TOP]
    segments[BOTTOM_LEFT] = segments[BOTTOM]

    # process signals with multiple occurences of the same length

    signal_zero = find_signal_of_length_using_only_one_value_of_each_sets(
        signal_patterns, 6, [segments[MIDDLE]])
    signal_two = find_signal_of_length_using_only_one_value_of_each_sets(
        signal_patterns, 5, [segments[TOP_LEFT], segments[BOTTOM_RIGHT]])
    signal_three = find_signal_of_length_using_only_one_value_of_each_sets(
        signal_patterns, 5, [segments[TOP_LEFT], segments[BOTTOM_LEFT]])
    signal_five = find_signal_of_length_using_only_one_value_of_each_sets(
        signal_patterns, 5, [segments[TOP_RIGHT], segments[BOTTOM_LEFT]])
    signal_six = find_signal_of_length_using_only_one_value_of_each_sets(
        signal_patterns, 6, [segments[TOP_RIGHT]])
    signal_nine = find_signal_of_length_using_only_one_value_of_each_sets(
        signal_patterns, 6, [segments[BOTTOM_LEFT]])

    signals = [set(signal_zero), set(signal_one), set(signal_two), set(signal_three), set(signal_four), set(
        signal_five), set(signal_six), set(signal_seven), set(signal_eight), set(signal_nine)]

    return signals


result = 0
for line in lines:
    signal_patterns_raw, output_values_raw = [
        s.strip() for s in line.split(' | ')]
    signal_patterns = signal_patterns_raw.split(' ')
    output_values = output_values_raw.split(' ')

    signals = map_signal_patterns(signal_patterns)

    sub_result_str = ''
    for output_value in output_values:
        for i in range(len(signals)):
            if signals[i] == set(output_value):
                sub_result_str += str(i)
                break

    result += int(sub_result_str)

print(result)
