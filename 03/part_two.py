import re


with open("input.txt") as f:
    lines = f.readlines()

result = 0

regex = r"mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)"

actual_cond = "enable"

for line in lines:
    cond_matches = []
    position = 0
    keywords = ["do()", "don't()"]

    while position < len(line):
        found_keywords = []

        for keyword in keywords:
            keyword_len = len(keyword)

            if (
                position + keyword_len <= len(line)
                and line[position : position + keyword_len] == keyword
            ):
                found_keywords.append((keyword, position))

        if found_keywords:
            if found_keywords[0][0] == "don't()":
                state = "disable"
            else:
                state = "enable"

            cond_matches.append((state, position))

            if state == "disable":
                position += len(keywords[1])
            else:
                position += len(keywords[0])
        else:
            position += 1

    matches = re.finditer(regex, line)

    for match in matches:
        for cond in cond_matches:
            if cond[1] < match.start():
                actual_cond = cond[0]
            if cond[1] > match.start():
                break

        if actual_cond == "enable":
            groupdict = match.groupdict()
            result += int(groupdict["first"]) * int(groupdict["second"])

print(result)
