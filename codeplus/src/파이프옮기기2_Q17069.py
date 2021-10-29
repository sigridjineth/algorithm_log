def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    d = [[[0] * 3 for _ in range(n)] for _ in range(n)]

    def solve():
        d[0][1][0] = 1
        for i in range(n):
            for j in range(n):
                if (j + 1 < n and a[i][j+1] == 0):
                    d[i][j+1][0] += (d[i][j][2] + d[i][j][0])
                if (i + 1 < n and a[i+1][j] == 0):
                    d[i+1][j][1] += (d[i][j][1] + d[i][j][2])
                if (i + 1 < n and j + 1 < n and a[i+1][j] == 0 and a[i+1][j+1] == 0 and a[i][j+1] == 0):
                    d[i+1][j+1][2] += (d[i][j][0] + d[i][j][1] + d[i][j][2])
    
    solve()
    return sum(d[n-1][n-1])

print(solution())
