from copy import deepcopy
import sys

def next_permutation(a):
    i = len(a) - 1
    while (i > 0 and a[i - 1] >= a[i]):
        i -= 1
    if (i <= 0):
        return False
    
    j = len(a) - 1
    while (a[j] <= a[i - 1]):
        j -= 1
    
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

def go(b, t):
    row, col, size = t
    groups = [[]]

    # size를 늘려나가며 single array initalization    
    for s in range(1, size + 1):
        group = []
        
        for c in range(col - s, col + s):
            group.append(b[row - s][c])
        
        for r in range(row - s, row + s):
            group.append(b[r][col + s])
        
        for c in range(col + s, col - s, -1):
            group.append(b[row + s][c])
        
        for r in range(row + s, row - s, -1):
            group.append(b[r][col - s])
        
        groups.append(group)
    
    # 회전은 slicing을 이용한다
    for s in range(1, size + 1):
        group = groups[s]
        group = group[-1:] + group[:-1] # last index to first index
        index = 0

        # 갱신하기
        for c in range(col - s, col + s):
            b[row - s][c] = group[index]
            index += 1
        
        for r in range(row - s, row + s):
            b[r][col + s] = group[index]
            index += 1
        
        for c in range(col + s, col - s, -1):
            b[row + s][c] = group[index]
            index += 1
        
        for r in range(row + s, row - s, -1):
            b[r][col - s] = group[index]
            index += 1

def solution():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    d = [list(map(int, input().split())) for _ in range(k)]
    d = [(r - 1, c - 1, s) for r, c, s in d]
    answer = sys.maxsize

    while True:
        b = deepcopy(a)
        for t in d:
            go(b, t)
        for i in range(n):
            s = sum(b[i])
            if (answer > s):
                answer = s
        if not next_permutation(d):
            break

    return answer

print(solution())
