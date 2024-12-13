import re
import itertools
import collections


with open("input.txt") as f:
    lines = f.readlines()


btn_re = r".+X\+(\d+), Y\+(\d+)"
prize_re = r".+X=(\d+), Y=(\d+)"

cases = []
case_ = collections.defaultdict(dict)

for line in lines:
    if line.startswith("Button A"):
        x, y = re.match(btn_re, line).groups()
        case_["btnA"]["x"] = int(x)
        case_["btnA"]["y"] = int(y)
    elif line.startswith("Button B"):
        x, y = re.match(btn_re, line).groups()
        case_["btnB"]["x"] = int(x)
        case_["btnB"]["y"] = int(y)
    elif line.startswith("Prize"):
        x, y = re.match(prize_re, line).groups()
        case_["prize"]["x"] = int(x)
        case_["prize"]["y"] = int(y)
    elif line == "\n":
        cases.append(case_)
        case_ = collections.defaultdict(dict)

cases.append(case_)


def check(case_, comb):
    btn_a = case_["btnA"]
    btn_b = case_["btnB"]

    x = comb[0] * btn_a["x"]
    y = comb[0] * btn_a["y"]

    x += comb[1] * btn_b["x"]
    y += comb[1] * btn_b["y"]

    if x == case_["prize"]["x"] and y == case_["prize"]["y"]:
        return comb[0] * 3 + comb[1]

    return None


combs = list(itertools.product(range(101), repeat=2))
res = 0

for case_ in cases:
    best = None
    for comb in combs:
        res_ = check(case_, comb)
        if not best:
            best = res_
        elif res_ and (res_ < best):
            best = res_

    if best:
        res += best

print(res)
