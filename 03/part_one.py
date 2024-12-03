import re


with open("input.txt") as f:
    lines = f.readlines()

result = 0

regex = r"mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)"

for line in lines:
    matches = re.finditer(regex, line)

    for match in matches:
        groupdict = match.groupdict()
        result += int(groupdict["first"]) * int(groupdict["second"])

print(result)
