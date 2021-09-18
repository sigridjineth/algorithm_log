from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, x, y, size):
    n = len(a)
    ans = []
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    d[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                ok = False
                eat = False
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
                if a[nx][ny] == 0: 
                    ok = True
                elif a[nx][ny] < size: # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
                    ok = True
                    eat = True
                elif a[nx][ny] == size: # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                    ok = True
                if ok:
                    q.append((nx,ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny],nx,ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
x,y = 0,0
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x,y = i,j
            a[i][j] = 0
ans = 0
size = 2
exp = 0
while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1
    if size == exp:
        size += 1
        exp = 0
    x,y = nx,ny
print(ans)
