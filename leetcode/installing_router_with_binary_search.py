# 공유기 설치: 이진탐색 이용
n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

def find_distance(data, c):
    min_gap = abs(data[1]-data[0])
    max_gap = abs(data[-1]-data[0])
    result = 0

    while (min_gap <= max_gap):
        mid_gap = (min_gap + max_gap) // 2
        current_max_installed_value = data[0] # 첫 번째 집에는 무조건 공유기를 설치해서 최대 거리로 만든다.
        router_count = 1 # 일단 하나를 설치한다
        # 설치
        for i in range(1, len(data)):
            if (data[i] >= current_max_installed_value + mid_gap):
                current_max_installed_value = data[i] # 설치했음을 알려주고
                router_count += 1 # 라우터를 하나 올린다
        # 비교
        if (router_count >= c):
            min_gap = mid_gap + 1
            result = mid_gap # 현재 mid 값을 함수의 프로퍼티인 result에 저장해준다.

        else:
            max_gap = mid_gap - 1
        
    return result

print(find_distance(data, c))