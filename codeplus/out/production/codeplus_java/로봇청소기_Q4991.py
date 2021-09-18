from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def bfs(a, sx, sy):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and a[nx][ny] != 'x':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = [input() for _ in range(n)]
    b = [(0,0)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'o':
                b[0] = (i,j)
            elif a[i][j] == '*':
                b.append((i,j))
    l = len(b)
    d = [[0]*l for _ in range(l)]
    ok = True
    for i in range(l):
        dist = bfs(a,b[i][0], b[i][1])
        for j in range(l):
            d[i][j] = dist[b[j][0]][b[j][1]]
            if d[i][j] == -1:
                ok = False
    if not ok:
        print(-1)
        continue
    p = [i+1 for i in range(l-1)]
    ans = -1
    while True:
        now = d[0][p[0]]
        for i in range(l-2):
            now += d[p[i]][p[i+1]]
        if ans == -1 or ans > now:
            ans = now
        if not next_permutation(p):
            break
    print(ans)
