from collections import defaultdict


with open("input.txt") as f:
    lines = f.readlines()


rows = []

for line in lines:
    rows.append(line.strip())

row_count = len(rows)
col_count = len(rows[0])

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


def find_full_region(row_index, col_index, char):
    visited = set()
    incomplete_paths = [(row_index, col_index)]
    boundaries = defaultdict(list)

    while incomplete_paths:
        actual_position = incomplete_paths[0]
        row_index = actual_position[0]
        col_index = actual_position[1]
        visited.add((row_index, col_index))

        for d in directions:
            next_row_index = actual_position[0] + d[0]
            next_col_index = actual_position[1] + d[1]

            if (next_row_index > (row_count - 1)) or (next_row_index < 0):
                boundaries[d].append((row_index, col_index))
                continue
            if (next_col_index > (col_count - 1)) or (next_col_index < 0):
                boundaries[d].append((row_index, col_index))
                continue

            next_position = (next_row_index, next_col_index)
            next_val = rows[next_position[0]][next_position[1]]
            if (
                (next_val == char)
                and (next_position not in visited)
                and (next_position not in incomplete_paths)
            ):
                incomplete_paths.append(next_position)
            elif next_val != char:
                boundaries[d].append((row_index, col_index))

        incomplete_paths.pop(0)

    sides = 0
    for direction, positions in boundaries.items():
        processed = []
        for position in sorted(positions):
            if position in processed:
                continue

            sides += 1
            processed.append(position)

            if direction in ((-1, 0), (1, 0)):
                candidates = sorted(filter(lambda x: x[0] == position[0], positions))
                actual = position[1]
                for can in candidates:
                    if can[1] == actual + 1:
                        processed.append(can)
                        actual += 1
            elif direction in ((0, -1), (0, 1)):
                candidates = sorted(filter(lambda x: x[1] == position[1], positions))
                actual = position[0]
                for can in candidates:
                    if can[0] == actual + 1:
                        processed.append(can)
                        actual += 1

    price = sides * len(visited)
    return visited, price


res = 0

already_in_region = set()

for row_index, row in enumerate(rows):
    for col_index, char in enumerate(row):
        if (row_index, col_index) in already_in_region:
            continue

        visited, price = find_full_region(row_index, col_index, char)
        for v in visited:
            already_in_region.add(v)

        res += price

print(res)
