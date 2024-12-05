with open("input.txt") as f:
    lines = f.readlines()

keyword = "MAS"
res = 0

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char == "A":
            diagonal_a = ""
            diagonal_b = ""
            try:
                diagonal_a = (
                    lines[line_index - 1][char_index - 1]
                    + "A"
                    + lines[line_index + 1][char_index + 1]
                )
                diagonal_b = (
                    lines[line_index - 1][char_index + 1]
                    + "A"
                    + lines[line_index + 1][char_index - 1]
                )

                if ((line_index - 1) < 0) or ((char_index - 1) < 0):
                    continue

                if ((diagonal_a == keyword) or (diagonal_a == keyword[::-1])) and (
                    (diagonal_b == keyword) or (diagonal_b == keyword[::-1])
                ):
                    res += 1
            except:
                continue

print(res)
