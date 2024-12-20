with open("input.txt") as f:
    lines = f.readlines()


moves_flag = False
grid = []
moves = []
robot_position = None

for line_index, line in enumerate(lines):
    if line == "\n":
        moves_flag = True

    if not moves_flag:
        for char_index, char in enumerate(line.strip()):
            if char == "@":
                robot_position = (line_index, char_index)

        grid.append([char for char in line.strip()])
    else:
        moves.extend([char for char in line.strip()])


for move in moves:
    if move == "<":
        direction = (0, -1)
    elif move == ">":
        direction = (0, 1)
    elif move == "^":
        direction = (-1, 0)
    elif move == "v":
        direction = (1, 0)
    else:
        raise

    no_move = False
    boxes = []
    new_position = (robot_position[0] + direction[0], robot_position[1] + direction[1])

    while True:
        if grid[new_position[0]][new_position[1]] == "O":
            boxes.append(new_position)
        elif grid[new_position[0]][new_position[1]] == "#":
            no_move = True
            break
        elif grid[new_position[0]][new_position[1]] == ".":
            break
        else:
            raise

        new_position = (new_position[0] + direction[0], new_position[1] + direction[1])

    if not no_move:
        for box in reversed(boxes):
            grid[box[0]][box[1]] = "."
            grid[box[0] + direction[0]][box[1] + direction[1]] = "O"

        grid[robot_position[0]][robot_position[1]] = "."
        grid[robot_position[0] + direction[0]][robot_position[1] + direction[1]] = "@"
        robot_position = (
            robot_position[0] + direction[0],
            robot_position[1] + direction[1],
        )


res = 0
for line_index, line in enumerate(grid):
    for char_index, char in enumerate(line):
        if char == "O":
            res += 100 * line_index + char_index


print(res)
