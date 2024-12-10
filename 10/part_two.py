with open("input.txt") as f:
    lines = f.readlines()


rows = []

for line_index, line in enumerate(lines):
    rows.append([])
    for char in line:
        if char != "\n":
            rows[line_index].append(char)


directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


def find_hiking_trails(row_index, col_index):
    count = 0
    end_positions = set()

    incomplete_paths = [(row_index, col_index)]

    while incomplete_paths:
        actual_path = incomplete_paths[0]
        row_index = actual_path[0]
        col_index = actual_path[1]
        actual_val = rows[row_index][col_index]

        if actual_val == "9":
            count += 1
            end_positions.add((row_index, col_index))
            incomplete_paths.pop(0)
            continue

        for d in directions:
            if ((row_index + d[0]) > (len(rows) - 1)) or (row_index + d[0] < 0):
                continue
            if ((col_index + d[1]) > (len(rows[0]) - 1)) or (col_index + d[1] < 0):
                continue

            next_position = (row_index + d[0], col_index + d[1])
            next_val = rows[next_position[0]][next_position[1]]
            if int(next_val) - 1 == int(actual_val):
                incomplete_paths.append(next_position)

        incomplete_paths.pop(0)

    return count


res = 0

for row_index, row in enumerate(rows):
    for col_index, val in enumerate(row):
        if val == "0":
            res += find_hiking_trails(row_index, col_index)

print(res)
