# 화성 탐사
import heapq

def solution():
    INF = int(1e9)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    answer = []

    for _ in range(int(input())):
        # 노드의 개수를 입력받는다.
        n = int(input())

        # 전체 맵의 정보를 입력받는다.
        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))

        # 최단 거리 테이블을 초기화한다. 이 때 무한으로 초기화한다
        data = [[INF] * (n) for _ in range(n)]
        # 시작 위치를 초기화한다. 이 때 (0, 0)이다.
        x, y = 0, 0
        # 시작 노드로 가기 위한 비용은 (0, 0)의 위치 값이다. 이를 큐에 먼저 삽입한다.
        q = [(graph[x][y], x, y)]
        data[x][y] = graph[x][y]

        # 다익스트라 알고리즘을 수행
        while q:
            # 가장 최단 거리에 대한 데이터를 꺼내기
            dist, x, y = heapq.heappop(q)
            # dist가 지금 기록된 녀석보다 크다면 무시한다
            if (data[x][y] < dist):
                continue
            # 현재 노드와 연결된 다른 인접한 노드를 확인한다
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 맵의 범위를 벗어나는 경우 무시한다
                if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= n):
                    continue
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리
                cost = dist + graph[nx][ny]
                # 만약, 이렇게 계산해서 cost가 된 녀석이 기존 녀석보다 더 짧다면
                if (cost < data[nx][ny]):
                    data[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
        answer.append(data[n-1][n-1])
        
    return answer

print(solution())