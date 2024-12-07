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


for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char == "^":
            position = (line_index, char_index)

visited_positions = set()
visited_positions.add(position)

direction = "^"

while True:
    next_position_indexes = get_next_indexes(direction, position)
    try:
        next_position = lines[next_position_indexes[0]][next_position_indexes[1]]
    except IndexError:
        break

    new_right_position = None

    while not new_right_position:
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
            next_position = lines[next_position_indexes[0]][next_position_indexes[1]]
        else:
            new_right_position = next_position_indexes
            break

    visited_positions.add(new_right_position)
    position = new_right_position

res = len(visited_positions)
print(res)
