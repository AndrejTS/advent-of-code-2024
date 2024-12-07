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


def get_correct_order(rules):
    correct_order = []
    index = 0

    while rules:
        if index > (len(rules) - 1):
            index = 0
        rule = rules[index]
        page_a, page_b = rule.split()[0].split("|")
        for rule in rules:
            if page_a == rule.split()[0].split("|")[1]:
                index += 1
                break
        else:
            correct_order.append(page_a)
            indexes_to_delete = []
            for index_, rule in enumerate(rules):
                if page_a == rule.split()[0].split("|")[0]:
                    indexes_to_delete.append(index_)

            for i in sorted(indexes_to_delete, reverse=True):
                if len(rules) == 1:
                    correct_order.append(rule.split()[0].split("|")[1])
                del rules[i]

    return correct_order


for update in updates:
    if not check_update(update):
        used_rules = []
        for rule in rules:
            page_a, page_b = rule.split()[0].split("|")
            page_a_used = False
            page_b_used = False
            for page_num in update.split()[0].split(","):
                if not page_a_used and page_a == page_num:
                    page_a_used = True
                if not page_b_used and page_b == page_num:
                    page_b_used = True
            if page_a_used and page_b_used:
                used_rules.append(rule)

        correct_order = get_correct_order(used_rules)
        res += int(correct_order[(len(correct_order) // 2)])

print(res)
