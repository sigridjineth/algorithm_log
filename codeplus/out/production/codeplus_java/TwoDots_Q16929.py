dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())
a = [input() for _ in range(n)]
check = [[False]*m for _ in range(n)]

def go(x, y, px, py, color):
    if check[x][y]:
        return True
    check[x][y] = True
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if (nx,ny) == (px,py):
                continue
            if a[nx][ny] == color:
                if go(nx,ny,x,y,color):
                    return True
    return False

for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue
        ok = go(i, j, -1, -1, a[i][j])
        if ok:
            print('Yes')
            exit()
print('No')
