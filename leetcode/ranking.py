# 정확한 순위
def solution():
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == j):
                graph[i][j] = 0

    # 각 간선에 대한 정보를 입력받은 후, 그 값으로 초기화
    for _ in range(m):
        # A에서 B로 가는 비용을 1로 초기화
        a, b = map(int, input().split())
        graph[a][b] = 1

    # 점화식에 따라 플로이드-워셜 알고리즘을 수행
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

    result = 0
    # 각 학생들 번호를 하나씩 순회하면서 도달 가능한지 확인
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if (graph[i][j] != INF or graph[j][i] != INF): # A에서 B나 B에서 A로 도달 가능하면 성적 비교 가능
                count += 1
        if (count == n):
            result += 1

    return result

print(solution())