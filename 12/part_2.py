from queue import Queue

input_file = open('12/input.txt', 'r')

lines = input_file.readlines()

bigraph = {}

for line in lines:
    a, b = line.strip().split('-')

    if a in bigraph:
        bigraph[a].add(b)
    else:
        bigraph[a] = set([b])

    if b in bigraph:
        bigraph[b].add(a)
    else:
        bigraph[b] = set([a])

def rec(node, visited, second_visit_done):
    if node == 'end':
        # print(','.join(visited))
        return 1
    else:
        visited_set = set(visited)
        local_count = 0
        for candidate in bigraph[node]:
            # can I visit this candidate ?
            if candidate != 'start':
                if not (candidate.islower() and candidate in visited_set):
                    new_visited = visited[:]
                    new_visited.append(candidate)
                    local_count += rec(candidate, new_visited, second_visit_done)
                elif not second_visit_done:
                    new_visited = visited[:]
                    new_visited.append(candidate)
                    local_count += rec(candidate, new_visited, True)

        return local_count


paths_count = rec('start', ['start'], False)


print(paths_count)
