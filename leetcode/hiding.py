import heapq

INF = int(1e9)

def solution():
    n, m = map(int, input().split())
    start = 1
    # 노드에 대한 정보를 담는다
    graph = [[] for _ in range(n+1)]
    # 최단 거리 테이블 모두 무한으로 초기화
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        # a번 노드와 b번 노드는 상호 간에 비용이 1이라는 것을 말해주기 (사실 1이니까 BFS/DFS 써도 무방함)
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    dijkstra(start, distance, graph)

    # 동빈이가 숨을 최단 거리가 가장 먼 번호
    max_node = 0
    # 도달 가능한 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
    max_distance = 0
    # 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 갖는 노드들의 리스트
    result = []

    for i in range(1, n+1):
        if (max_distance < distance[i]):
            max_node = i
            max_distance = distance[i]
            result = [max_node]
        elif (max_distance == distance[i]):
            result.append(i)

    return (max_node, max_distance, len(result))

def dijkstra(start, distance, graph):
    q = []
    # 시작 노드로 가기 위해서 최단 경로는 0으로 설정하여 우선순위 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        # 현재 노드와 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 경우가 더 짧은 경우
            if (cost < distance[i[0]]):
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

print(solution())