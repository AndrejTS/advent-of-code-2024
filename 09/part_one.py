with open("input.txt") as f:
    lines = f.readlines()


disk_map = lines[0]
blocks_repr = []

cur_id = 0

for i, char in enumerate(disk_map):
    for k in range(int(char)):
        if (i % 2) == 0:  # file
            blocks_repr.append(str(cur_id))
        else:  # free space
            blocks_repr.append(".")
    if (i % 2) == 0:
        cur_id += 1


blocks_repr_len = len(blocks_repr)


def find_next_free_index(cur_index):
    cur_index += 1
    for i in range(cur_index, blocks_repr_len):
        if blocks_repr[i] == ".":
            return i


cur_free_index = find_next_free_index(-1)

block_to_move_index = -1


while True:
    if (blocks_repr_len + block_to_move_index) <= cur_free_index:
        break

    while True:
        if blocks_repr[block_to_move_index] != ".":
            block_to_move = blocks_repr[block_to_move_index]
            break
        else:
            block_to_move_index -= 1
            if (blocks_repr_len + block_to_move_index) <= cur_free_index:
                break

    blocks_repr[cur_free_index] = block_to_move
    blocks_repr[block_to_move_index] = "."
    cur_free_index = find_next_free_index(cur_free_index)
    block_to_move_index -= 1


res = 0
for i, char in enumerate(blocks_repr):
    if char == ".":
        break
    res += i * int(char)

print(res)
