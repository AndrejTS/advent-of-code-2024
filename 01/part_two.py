with open("input.txt") as f:
    lines = f.readlines()

left_row = []
right_row = []

for line in lines:
    left, right = line.split()
    left_row.append(left)
    right_row.append(right)

similarity_score = 0

for i in range(len(left_row)):
    similarity_score += int(left_row[i]) * right_row.count(left_row[i])

print(similarity_score)
