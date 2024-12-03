def check_report(report):
    direction = None

    for i in range(len(report) - 1):
        level = int(report[i])
        next_level = int(report[i + 1])

        level_diff = abs(level - next_level)
        if (level_diff > 3) or (level_diff < 1):
            return False

        if not direction:
            if level < next_level:
                direction = "inc"
            elif level > next_level:
                direction = "dec"
            else:
                return False

        if (level < next_level) and (direction != "inc"):
            return False
        elif (level > next_level) and (direction != "dec"):
            return False

    return True


with open("input.txt") as f:
    lines = f.readlines()

safe_reports_count = 0

for line in lines:
    report = line.split()
    if check_report(report):
        safe_reports_count += 1

print(safe_reports_count)
