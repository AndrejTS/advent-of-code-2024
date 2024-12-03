with open("input.txt") as f:
    lines = f.readlines()

left_row = []
right_row = []

for line in lines:
    left, right = line.split()
    left_row.append(left)
    right_row.append(right)

left_row.sort()
right_row.sort()

distance = 0

for i in range(len(left_row)):
    distance += abs(int(left_row[i]) - int(right_row[i]))

print(distance)
