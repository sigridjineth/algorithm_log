# 어두운 길
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
    n, m = map(int, input().split())
    parent = [0] * (n+1)

    for i in range(1, n+1):
        parent[i] = i

    edges = []
    result = 0

    for _ in range(m):
        x, y, cost = map(int, input().split())
        edges.append((cost, x, y)) # 비용순으로 정렬하기 위해 비용을 먼저 넣음

    edges.sort()
    total = 0

    for edge in edges:
        cost, a, b = edge
        total += cost
        
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(total - result)

solution()