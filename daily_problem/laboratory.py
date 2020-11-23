# 연구소
import copy

n, m = map(int, input().split())
data = []
result = -1

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 깊이 우선 탐색인 DFS를 활용해 각 바이러스가 사방으로 퍼지도록 처리
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dyr[i]
        # 4가지 방향 중에서 바이러스가 퍼질 수 있는 경우 체크
        if (nx >= 0) and (nx < n) and (ny >= 0) and (ny < m):
            if (temp[nx][ny] == 0):
                temp[nx][ny] = 2
                virus(nx, ny) # 바이러스를 전파시키고 재귀적으로 수행

# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_safe_area():
    score = 0
    for i in range(n):
        for j in range(m):
            if (temp[i][j] == 0):
                score += 1
    return score

# 깊이 우선 탐색 DFS를 이용해서 울타리를 설치하고 매번 안전 영역의 크기를 계산
def dfs(count):
    global temp
    global result # 전역 변수를 지역 단위에서 사용하고 싶으면 global keyword를 붙여야 한다

    # 울타리가 3개 설치된 경우
    if (count == 3):
        temp = copy.deepcopy(data)
        # 각 바이러스에서 위치 전파 실행
        for i in range(n):
            for j in range(m):
                if (temp[i][j] == 2):
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_safe_area())
        return result
    
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m): # 모든 경우의 수를 다 돌아보는 것
            if (data[i][j] == 0):
                data[i][j] = 1
                count += 1
                dfs(count) # 재귀적 실행
                # 다 돌았으면 다시 돌아와서 다음 녀석을 수행
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)