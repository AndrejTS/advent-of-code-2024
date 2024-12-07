with open("input.txt") as f:
    lines = f.readlines()

res = 0
rules = []
updates = []

flag_on = False

for line in lines:
    if line == "\n":
        flag_on = True
        continue
    if flag_on:
        updates.append(line)
        continue

    rules.append(line)

# print(rules)
# print(updates)


def check_update(update):
    for page_num in update.split()[0].split(","):
        for rule in rules:
            page_a, page_b = rule.split()[0].split("|")
            if page_num == page_a:
                check_num = page_a
            elif page_num == page_b:
                check_num = page_b
            else:
                continue

            if check_num == page_a:
                page_b_in_update = update.find(page_b)
                if page_b_in_update != -1:
                    if update.find(page_num) > update.find(page_b):
                        return False
            elif check_num == page_b:
                page_a_in_update = update.find(page_a)
                if page_a_in_update != -1:
                    if update.find(page_num) < update.find(page_a):
                        return False
    return True


for update in updates:
    if check_update(update):
        update = update.split()[0].split(",")
        res += int(update[(len(update) // 2)])

print(res)
