# 안테나
import copy

n = int(input())
data = list(map(int, input().split()))
result = []

for house in data:
    now = house
    temp = copy.deepcopy(data)
    temp.remove(now)
    now_sum = 0
    for other in temp:
        now_sum += abs(now - other)
    result.append((now, temp))

result.sort(key = lambda x: x[1])

print(result[0][0])

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# 중간값을 출력하면 된다. 단순히 모든 집의 위치 정보를 입력받은 뒤에, 중간값을 출력한다. 중간값에서 멀어지면 총합은 계속 증가하게 된다
# print(data[(n-1) // 2])