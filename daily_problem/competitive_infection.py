# competitive infection
# 방문하지 않은 노드를 차례대로 방문하면서 BFS를 구현한다.

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담은 리스트
data = [] # 바이러스에 대한 정보를 담은 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if (graph[i][j] != 0):
            # 바이러스 종류, 시간(0초), 위치 i, 위치 j 삽입
            data.append((graph[i][j], 0, i, j))

data.sort() # 낮은 번호의 바이러스가 먼저 증식하므로 정렬 이후에 큐로 옮긴다.
q = deque(data)

target_time, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색 BFS 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 S초가 지나거나
    # 큐가 빌 때까지 반복
    if s == target_time:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if (nx >= 0) and (nx < n) and (ny >= 0) and (ny < n):
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if (graph[nx][ny] == 0):
                graph[nx][ny] = virus
                # 인접 노드로 큐에 넣기
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])    