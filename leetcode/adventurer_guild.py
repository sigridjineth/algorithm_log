# 모험가 길드
# 그리디인 이유는, 가장 적은 공포도부터 체크해야 가장 최대의 그룹 수를 확인할 수 있기 때문이다.

n = int(input())
data = list(map(int, input().split()))

# 공포도에 따라 오름차순으로 정렬
data.sort()

# 총 그룹의 수를 초기화
result = 0

# 현재 그룹에 포함된 모험가의 수를 초기화
current_group_adventurer = 0

# 정렬된 공포도 리스트를 하나씩 순회
for i in data:
    # 만약 현재 그룹 도전자들의 수에서 새 도전자를 추가하는 것이
    # 현재 체크하고 있는 공포도보다 같거나 많다면 현재 그룹의 최대치인 것
    if (current_group_adventurer + 1 >= i):
        result += 1
        current_group_adventurer = 0
    else:
        current_group_adventurer += 1

print(result)
