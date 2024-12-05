with open("input.txt") as f:
    lines = f.readlines()

keyword = "XMAS"
res = 0
directions = (
    (+1, 0),
    (-1, 0),
    (0, +1),
    (0, -1),
    (+1, +1),
    (-1, -1),
    (+1, -1),
    (-1, +1),
)

# hor
(+1, 0), (-1, 0)
# vertical
(0, +1), (0, -1)
# diagonal
(+1, +1), (-1, -1), (+1, -1), (-1, +1)

# print(lines)

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char == "X":
            for direction in directions:
                word = "X"
                cur_line_index = line_index
                cur_char_index = char_index
                try:
                    for _ in range(len(keyword) - 1):
                        cur_line_index += direction[1]
                        cur_char_index += direction[0]
                        if (cur_line_index < 0) or (cur_char_index < 0):
                            break
                        word += lines[cur_line_index][cur_char_index]
                    if word == "XMAS":
                        res += 1
                except:
                    continue

print(res)
