from collections import deque

# 도시 개수 n, 도로 개수 m, 거리 정보 k, 출발 도시 번호 x
n, m, k, x = map(int, input().split())

# 도시마다 새로운 graph를 만든다
graph = [[] for _ in range(n+1)]

# 모든 도로의 정보를 입력받는다
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리를 -1로 초기화한다
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시에서 출발 도시까지의 거리는 0으로 설정한다.

# 너비 우선 탐색 BFS를 실행한다
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 노드라면
        if (distance[next_node] == -1):
            # 최단 거리를 방문하고 갱신한다
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 정렬한다
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)