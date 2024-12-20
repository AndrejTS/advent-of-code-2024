import re


with open("input.txt") as f:
    lines = f.readlines()


regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

robots = []
for line in lines:
    x, y, vx, vy = re.match(regex, line).groups()
    robots.append({"x": int(x), "y": int(y), "vx": int(vx), "vy": int(vy)})


for robot in robots:
    for _ in range(100):
        new_x = robot["x"] + robot["vx"]
        if new_x > 100:
            new_x -= 101
        if new_x < 0:
            new_x += 101
        robot["x"] = new_x

        new_y = robot["y"] + robot["vy"]
        if new_y > 102:
            new_y -= 103
        if new_y < 0:
            new_y += 103
        robot["y"] = new_y

quadrant_1 = []
quadrant_2 = []
quadrant_3 = []
quadrant_4 = []

for robot in robots:
    if robot["x"] == 50:
        continue
    if robot["y"] == 51:
        continue

    is_left = False
    is_right = False
    is_top = False
    is_down = False

    if robot["x"] < 50:
        is_left = True
    else:
        is_right = True
    if robot["y"] < 51:
        is_top = True
    else:
        is_down = True

    if is_top and is_left:
        quadrant_1.append(robot)
    if is_top and is_right:
        quadrant_2.append(robot)
    if is_down and is_left:
        quadrant_3.append(robot)
    if is_down and is_right:
        quadrant_4.append(robot)


print(len(quadrant_1))
print(len(quadrant_2))
print(len(quadrant_3))
print(len(quadrant_4))

print(len(quadrant_1) * len(quadrant_2) * len(quadrant_3) * len(quadrant_4))
