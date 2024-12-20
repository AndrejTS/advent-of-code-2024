import re


with open("input.txt") as f:
    lines = f.readlines()


regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

robots = []
for line in lines:
    x, y, vx, vy = re.match(regex, line).groups()
    robots.append({"x": int(x), "y": int(y), "vx": int(vx), "vy": int(vy)})


for iii in range(100000):
    grid = [["." for _ in range(101)] for _ in range(103)]

    for robot in robots:
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

        grid[robot["y"]][robot["x"]] = "*"

    neighbor_score = 0
    for robot in robots:
        robot_x = robot["x"]
        robot_y = robot["y"]
        for robot_ in robots:
            robot_y_diff = abs(robot_y - robot_["y"])
            if robot_y_diff < 2:
                if abs(robot_x - robot_["x"]) < 2:
                    neighbor_score += 1

    if neighbor_score > 1100:
        for i in grid:
            print("".join(i))
        print(iii, neighbor_score, "#" * 50)
