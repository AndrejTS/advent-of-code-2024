from functools import cache


with open("input.txt") as f:
    lines = f.readlines()


stones = lines[0].split()

res = 0


@cache
def blink(stone):
    stones = []
    if stone == "0":
        stones = ["1"]
    elif (len(stone) % 2) == 0:
        number_len = len(stone)
        left = str(int(stone[: (number_len // 2)]))
        right = str(int(stone[(number_len // 2) :]))
        stones = [left, right]
    else:
        stones = [str(int(stone) * 2024)]

    return stones


@cache
def process_stone(stone, remaining_blinks):
    if remaining_blinks == 0:
        return 1

    stones = blink(stone)

    res = 0
    for stone in stones:
        res += process_stone(stone, remaining_blinks - 1)

    return res


for stone in stones:
    res += process_stone(stone, 75)

print(res)
