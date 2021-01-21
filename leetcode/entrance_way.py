# 탑승구
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
    g = int(input())
    p = int(input())
    parent = [0] * (g+1) # 탑승구의 숫자만큼 초기화. 여기서 루트가 0일 때 더 이상 도킹이 불가능하다고 판단
    result = 0

    # 부모 테이블 상에서 자기 자신을 초기화
    for i in range(1, g+1):
        parent[i] = i
    for _ in range(0, p):
        now_range = int(input())
        now_root = find_parent(parent, now_range)
        if (now_root == 0):
            break
        else:
            union_parent(parent, now_root, now_root - 1) # 바로 옆에 있는 노드와 합집합 연산을 수행한다.
            result += 1

    return result

print(solution())