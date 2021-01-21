# 행성 터널
def find_parent(parent, x):
    if (parent[x] != x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

def solution():
    n = int(input())
    parent = [0] * (n+1) # 부모 테이블 초기화

    edges = []
    result = 0

    for i in range(1, n+1):
        parent[i] = i

    x = []
    y = []
    z = []

    # 모든 노드에 대한 좌표 값을 입력받는다.
    for i in range(1, n+1):
        x_value, y_value, z_value = map(int, input().split())
        x.append((x_value, i))
        y.append((y_value, i))
        z.append((z_value, i))

    x.sort()
    y.sort()
    z.sort()

    # 인접한 노드들로부터 간선 정보를 추출하여, 비용 순으로 정렬한다.
    for i in range(n-1):
        edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
        edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
        edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

    # 간선을 비용 순으로 정렬
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if (find_parent(parent, a) != find_parent(parent, b)):
            union_parent(parent, a, b)
            result += cost
    
    return result