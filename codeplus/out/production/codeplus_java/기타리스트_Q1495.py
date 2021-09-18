def solution():
    n, s, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    d = [[False] * (m + 1) for _ in range(n + 1)]
    d[0][s] = True
    for i in range(n):
        for j in range(m + 1):
            if (d[i][j] == False):
                continue
            if (j - a[i + 1] >= 0):
                d[i + 1][j - a[i + 1]] = True
            if (j + a[i + 1] < m + 1):
                d[i + 1][j + a[i + 1]] = True
    ans = -1
    for i in range(m + 1):
        if (d[n][i] == True):
            ans = i
    return ans

print(solution())
