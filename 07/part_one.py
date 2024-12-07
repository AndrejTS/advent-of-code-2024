from itertools import product

with open("input.txt") as f:
    lines = f.readlines()

res = 0

operators = ["+", "*"]


def check(test_value, numbers, comb_of_operators):
    numbers = [int(x) for x in numbers]

    for comb in comb_of_operators:
        res = numbers[0]
        for index in range(1, len(numbers)):
            operator = comb[index - 1]
            if operator == "+":
                res += numbers[index]
            elif operator == "*":
                res *= numbers[index]

        if res == int(test_value):
            return True


for line in lines:
    test_value, numbers = line.split(":")
    numbers = numbers.split()

    number_of_operators = len(numbers) - 1

    comb_of_operators = product(operators, repeat=number_of_operators)

    if check(test_value, numbers, comb_of_operators):
        res += int(test_value)

print(res)
