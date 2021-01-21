def solution():
    INF = int(1e9)
    n = int(input())
    m = int(input())
    # 2차원 리스트 만들기
    data = [[INF] * (n+1) for _ in range(n+1)]

    # 자기 자신에서 가는 비용은 0으로 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == j):
                data[i][j] = 0
    
    # 각 간선에 대한 정보를 입력받은 뒤 최솟값만 입력해준다.
    for i in range(m):
        a, b, c = map(int, input().split())
        if (c < data[a][b]):
            data[a][b] = c
    
    # 플로이드-워셜 알고리즘을 적용
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                data[a][b] = min(data[a][b], data[a][k] + data[k][b])

    # 수행된 결과를 출력
    for a in range(1, n+1):
        for b in range(1, n+1):
            if (data[a][b] == INF):
                print(0, " ")
            else:
                print(data[a][b], " ")
            print()