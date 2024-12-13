import re
import collections
from decimal import Decimal


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
        case_["prize"]["x"] = int(x) + 10000000000000
        case_["prize"]["y"] = int(y) + 10000000000000
    elif line == "\n":
        cases.append(case_)
        case_ = collections.defaultdict(dict)

cases.append(case_)


def check(case_):
    btn_a = case_["btnA"]
    btn_b = case_["btnB"]

    coeffs = [[btn_a["x"], btn_b["x"]], [btn_a["y"], btn_b["y"]]]
    constants = [case_["prize"]["x"], case_["prize"]["y"]]

    def solve_linear_system(coeffs, constants):
        coeffs = [[Decimal(str(c)) for c in row] for row in coeffs]
        constants = [Decimal(str(c)) for c in constants]

        det = coeffs[0][0] * coeffs[1][1] - coeffs[0][1] * coeffs[1][0]

        a = (constants[0] * coeffs[1][1] - constants[1] * coeffs[0][1]) / det
        b = (coeffs[0][0] * constants[1] - coeffs[1][0] * constants[0]) / det

        return a, b

    result_a, result_b = solve_linear_system(coeffs, constants)

    return result_a, result_b


res = 0

for case_ in cases:
    result_a, result_b = check(case_)
    if (result_a == int(result_a)) and (result_b == int(result_b)):
        res_ = 3 * result_a + result_b
        res += res_

print(res)
