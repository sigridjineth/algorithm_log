from collections import deque
dx = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
cost = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
a = [[0] * 200 for _ in range(200)]
d = [[[-1] * 31 for _ in range(200)] for _ in range(200)]

l = int(input())
m, n = map(int, input().split())
a = []
for i in range(n):
    a.append((list(map(int, input().split()))))
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 0

while q:
    x, y, c = q.popleft()
    for k in range(4 + 8):
        nx = x + dx[k]
        ny = y + dy[k]
        nc = c + cost[k]

        if (0 <= nx < n and 0 <= ny < m):
            if (a[nx][ny] == 1):
                continue
            if (nc <= l):
                if (d[nx][ny][nc] == -1):
                    d[nx][ny][nc] = d[x][y][c] + 1
                    q.append((nx, ny, nc))

ans = -1
for i in range(l + 1):
    if (d[n - 1][m - 1][i] == -1):
        continue
    if (ans == -1 or ans > d[n - 1][m - 1][i]):
        ans = d[n - 1][m - 1][i]

print(ans)