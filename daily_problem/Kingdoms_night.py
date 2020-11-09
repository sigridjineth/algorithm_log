# Kingdom's night
input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
answer = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if (next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8):
        answer = answer + 1

print(answer)