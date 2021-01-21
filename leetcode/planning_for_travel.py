# planning for travel
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
        parent[i] = i # 자기 자신으로 초기화
    # union 연산을 각각 수행
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(n):
            if (data[j] == 1): # 연결되었다는 의미이므로
                union_parent(parent, i+1, j+1)

    plan = list(map(int, input().split()))
    result = True
    for i in range(m-1):
        if (find_parent(parent, plan[i]) != (find_parent(parent, plan[i+1]))):
            return False

    if (result == True):
        return "YES"
    else:
        return "NO"

print(solution())