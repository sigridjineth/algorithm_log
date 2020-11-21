# 치킨배달

from itertools import combinations

n, m = map(int, input().split())
chicken = []
house = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if (data[j] == 1):
            house.append((i,j))
        else:
            chicken.append((i,j))

# 모든 치킨집 중에서 m개를 뽑는 연산 수행
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0 # 결과값
    for x, y in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(x-cx) + abs(y-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)