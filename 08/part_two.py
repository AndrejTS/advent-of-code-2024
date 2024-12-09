with open("input.txt") as f:
    lines = f.readlines()


antenas = dict()

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if (char != ".") and (char != "\n"):
            if char not in antenas:
                antenas[char] = []
            antenas[char].append((line_index, char_index))

antinodes = set()

for antena_group in antenas:
    for antena in antenas[antena_group]:
        for antena_ in antenas[antena_group]:
            if antena_ == antena:
                continue

            antinodes.add(antena)
            antinodes.add(antena_)

            diff = (abs(antena[0] - antena_[0]), abs(antena[1] - antena_[1]))

            if antena[1] < antena_[1]:
                left_antena = antena
                right_antena = antena_
            elif antena[1] > antena_[1]:
                left_antena = antena_
                right_antena = antena

            if antena[0] < antena_[0]:
                up_antena = antena
                down_antena = antena_
            elif antena[0] > antena_[0]:
                up_antena = antena_
                down_antena = antena

            antinode_a = left_antena
            antinode_b = right_antena

            while True:
                if antinode_a:
                    if (
                        (antinode_a[0] < 0)
                        or (antinode_a[0] > (len(lines) - 1))
                        or (antinode_a[1] < 0)
                        or (antinode_a[1] > (len(lines[0].strip()) - 1))
                    ):
                        antinode_a = None
                if antinode_b:
                    if (
                        (antinode_b[0] < 0)
                        or (antinode_b[0] > (len(lines) - 1))
                        or (antinode_b[1] < 0)
                        or (antinode_b[1] > (len(lines[0].strip()) - 1))
                    ):
                        antinode_b = None

                if antinode_a:
                    antinodes.add(antinode_a)
                if antinode_b:
                    antinodes.add(antinode_b)

                if not antinode_a and not antinode_b:
                    break

                if left_antena == up_antena:
                    if antinode_a:
                        antinode_a = (antinode_a[0] - diff[0], antinode_a[1] - diff[1])
                    if antinode_b:
                        antinode_b = (antinode_b[0] + diff[0], antinode_b[1] + diff[1])
                elif left_antena == down_antena:
                    if antinode_a:
                        antinode_a = (antinode_a[0] + diff[0], antinode_a[1] - diff[1])
                    if antinode_b:
                        antinode_b = (antinode_b[0] - diff[0], antinode_b[1] + diff[1])


for ant in antinodes:
    line = lines[ant[0]]
    lines[ant[0]] = line[: ant[1]] + "#" + line[(ant[1] + 1) :]

for line_index, line in enumerate(lines):
    print(line.strip())


# print(antinodes)
print(len(antinodes))
