with open("input.txt") as f:
    lines = f.readlines()


stones = lines[0].split()

for _ in range(25):
    index = 0
    while index < len(stones):
        if stones[index] == "0":
            stones[index] = "1"
        elif (len(stones[index]) % 2) == 0:
            number_len = len(stones[index])
            left = str(int(stones[index][: (number_len // 2)]))
            right = str(int(stones[index][(number_len // 2) :]))
            stones[index] = left
            stones.insert(index + 1, right)
            index += 1
        else:
            stones[index] = str(int(stones[index]) * 2024)

        index += 1

print(len(stones))
