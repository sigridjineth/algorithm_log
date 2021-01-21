# 만들 수 없는 금액
n = int(input())
data = list(map(int, input().split()))
data.sort();

target = 1
for x in data:
    # 만들 수 없는 금액을 만났을 때는 반복문을 탈출한다.
    if (target < x):
        break
    else:
        target += x

print(target)
