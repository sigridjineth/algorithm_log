from collections import deque

def solution():
    n = int(input()) # 노드 개수 입력받기
    indegree = [0] * (n+1)

    graph = [[False]*(n+1) for _ in range(n+1)]
    data = list(map(int, input().split()))

    # 방향 그래프의 간선 정보를 초기화한다
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True # 연결한다
            indegree[data[i]] += 1

    # 올해 순위를 입력한다
    m = int(input())

    for i in range(m):
        a, b = map(int, input().split())

        if (graph[a][b] == True): # 서로 교체해준다.
            graph[a][b] = False
            graph[b][a] = True
            indegree[data[a]] += 1
            indegree[data[b]] -= 1
        
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[data[a]] -= 1
            indegree[data[b]] += 1

    answer = topology_sort(indegree, n, graph)

    if (answer == "CYCLE"):
        print("IMPOSSIBLE")
    elif (answer == "NOT_DECIDEABLE"):
        print("?")
    else:
        for i in answer:
            print(i, end = ' ')
        print()

def topology_sort(indegree, v, graph):
    result = []
    q = deque()

    # 처음 시작할 때 indegree = 0 노드를 넣는다.
    for i in range(1, v+1):
        if (indegree[i] == 0):
            q.append(i)

    cycle = False
    NOT_DECIDABLE = False

    # 정확히 노드 개수만큼 반복해야 한다.
    for i in range(v):
        # 예외의 경우 첫 번째: 큐가 전체 노드 개수를 돌기 전에 다 비게 되면 싸이클이 발생한다.
        # 새롭게 진입차수에 0이 되는 녀석이 없다는 것은 최소 진입차수가 1이라는 의미이고 뺑뻉 돈다는 소리이다.
        if (len(q) == 0):
            cycle = True
            break
        # 예외의 경우 두 번째: 큐에 2개 이상의 원소가 있다는 것은 순위를 정확하게 확정할 수 없다는 뜻이다.
        # 어느 원소를 먼저 처리하느냐에 따라 순위가 달라지기 때문이다.
        if (len(q) >= 2):
            NOT_DECIDABLE = True
            break
    
        # 큐에서 제거 후에 원소를 result에 넣는다.
        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if (graph[now][j] == True):
                indegree[j] -= 1 # True면 일단 현재 노드와 연결된 모든 노드의 진입차수를 1 낮춘다.
                if (indegree[j] == 0): # 만약 현재 노드의 진입차수가 0이라면
                    q.append(j) # 큐에 넣는다.

    if (cycle):
        return "CYCLE"
    elif (NOT_DECIDABLE):
        return "NOT_DECIDABLE"
    else:
        return result

solution()