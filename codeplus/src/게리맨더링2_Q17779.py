from collections import deque

def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = -1

    def bfs(d, x, y, g):
        d[x][y] = g
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.pop()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if (0 <= nx < n and 0 <= ny < n):
                    if (d[nx][ny] == 0):
                        d[nx][ny] = g
                        q.append((nx, ny))

    def go(a, x, y, d1, d2):
        d = [[0] * n for _ in range(n)]
        for i in range(d1 + 1):
            d[x + i][y - i] = 5
            d[(x + d2) + i][(y + d2) - i] = 5
        for i in range(d2 + 1):
            d[x + i][y + i] = 5
            d[(x + d1) + i][(y - d1) + i] = 5
        for j in range(0, y - d1):
            d[x + d1][j] = 3
        for i in range(0, x):
            d[i][y] = 1
        for j in range(y + d2 + 1, n):
            d[x + d2][j] = 2
        for i in range(x + d1 + d2 + 1, n):
            d[i][y - d1 + d2] = 4
        
        bfs(d, 0, 0, 1)
        bfs(d, 0, n - 1, 2)
        bfs(d, n - 1, 0, 3)
        bfs(d, n - 1, n - 1, 4)

        cnt = [0] * 5
        for i in range(n):
            for j in range(n):
                if (d[i][j] == 0):
                    d[i][j] = 5
                cnt[d[i][j] - 1] += a[i][j]
        
        cnt.sort()
        ans = cnt[-1] - cnt[0]
        return ans
    
    for x in range(n):
        for y in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    if (0 <= (y - d1) and (y + d2) < n):
                        if ((x + d1) + d2) < n:
                            temp = go(a, x, y, d1, d2)
                            if (ans == -1 or ans > temp):
                                ans = temp
    
    return ans

print(solution())
