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


def find_next_free_index(cur_index, blocks_count, limit):
    cur_index += 1
    for i in range(cur_index, blocks_repr_len):
        if i > limit:
            return
        if blocks_repr[i] == ".":
            if "".join(blocks_repr[i : i + blocks_count]) == "." * blocks_count:
                return i


cur_id -= 1
cur_index = len(blocks_repr) - 1

exceeding_len = None

for file_id in range(cur_id, -1, -1):
    file_indexes = []
    found = False
    for i in range(cur_index, -1, -1):
        if blocks_repr[i] == str(file_id):
            found = True
            k = i
            while True:
                file_indexes.append(k)
                k -= 1
                if k < 0:
                    break
                if blocks_repr[k] != str(file_id):
                    break
            cur_index = k
        if found:
            break

    if exceeding_len is not None:
        if len(file_indexes) >= exceeding_len:
            continue

    cur_free_index = find_next_free_index(-1, len(file_indexes), file_indexes[0])

    if not cur_free_index:
        exceeding_len = len(file_indexes)
        continue

    for i in range(len(file_indexes)):
        blocks_repr[cur_free_index + i] = str(file_id)
        blocks_repr[file_indexes[i]] = "."


res = 0
for i, char in enumerate(blocks_repr):
    if char == ".":
        continue
    res += i * int(char)

print(res)
