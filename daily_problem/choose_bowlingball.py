# 볼링공 고르기: 2019 소마 기출
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 0부터 10까지의 무게를 담을 수 있는 리스트 (Dynamic Programming과 유사)
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링 공의 개수를 카운트. 따라서 순서대로 정렬되는 효과가 있음.
    array[x] += 1

result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링 공의 개수, 즉 A가 선택할 수 있는 개수는 제외한다. 
    # 그리고 이미 계산한 것은 처리하지 않는다. A < B라고 간주한다.
    result += array[i] * n;

print(result)
