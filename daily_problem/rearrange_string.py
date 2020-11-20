# 문자열 재정렬
data = input()
alpha = []
value = 0

for x in data:
    if (x.isalpha()):
        alpha.append(x)
    else:
        value += int(x)

alpha.sort()

if (value != 0):
    alpha.append(str(value))

print(''.join(alpha))