with open("input.txt") as f:
    lines = f.readlines()


def get_next_indexes(direction, cur_position):
    if direction == "^":
        next_position_indexes = (cur_position[0] - 1, cur_position[1])
    if direction == "v":
        next_position_indexes = (cur_position[0] + 1, cur_position[1])
    if direction == ">":
        next_position_indexes = (cur_position[0], cur_position[1] + 1)
    if direction == "<":
        next_position_indexes = (cur_position[0], cur_position[1] - 1)

    return next_position_indexes


def check_is_in_loop(lines):
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "^":
                position = (line_index, char_index)

    visited_positions = set()
    visited_positions.add(position)

    direction = "^"
    obstacle_positions = []
    is_in_loop = False

    while True:
        if is_in_loop:
            return True

        next_position_indexes = get_next_indexes(direction, position)
        if (next_position_indexes[0] < 0) or (next_position_indexes[1] < 0):
            return False
        try:
            next_position = lines[next_position_indexes[0]][next_position_indexes[1]]
        except IndexError:
            return False

        new_right_position = None

        while not new_right_position:
            if is_in_loop:
                return True

            if next_position == "#":
                if direction == "^":
                    direction = ">"
                elif direction == "v":
                    direction = "<"
                elif direction == ">":
                    direction = "v"
                elif direction == "<":
                    direction = "^"

                next_position_indexes = get_next_indexes(direction, position)
                if (next_position_indexes[0] < 0) or (next_position_indexes[1] < 0):
                    return False
                next_position = lines[next_position_indexes[0]][
                    next_position_indexes[1]
                ]

                if (direction, position) in obstacle_positions:
                    is_in_loop = True
                obstacle_positions.append((direction, position))
            else:
                new_right_position = next_position_indexes
                break

        visited_positions.add(new_right_position)
        position = new_right_position


res = 0

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char == ".":
            line_list = list(line)
            line_list[char_index] = "#"
            line_ = "".join(line_list)
            lines[line_index] = line_

            if check_is_in_loop(lines):
                res += 1

            lines[line_index] = line


print(res)
