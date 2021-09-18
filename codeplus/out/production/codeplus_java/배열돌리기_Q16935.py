def operation1(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = a[n-i-1][j]
    return ans

def operation2(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = a[i][m-j-1]
    return ans

def operation3(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[n-j-1][i]
    return ans

def operation4(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[j][m-i-1]
    return ans

def operation5(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j+m//2] = a[i][j]
            ans[i+n//2][j+m//2] = a[i][j+m//2]
            ans[i+n//2][j] = a[i+n//2][j+m//2]
            ans[i][j] = a[i+n//2][j]
    return ans

def operation6(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i+n//2][j] = a[i][j]
            ans[i][j] = a[i][j+m//2]
            ans[i][j+m//2] = a[i+n//2][j+m//2]
            ans[i+n//2][j+m//2] = a[i+n//2][j]
    return ans

n,m,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
func = [operation1, operation2, operation3, operation4, operation5, operation6]
for op in map(int, input().split()):
    a = func[op-1](a)
for row in a:
    print(*row, sep=' ')
    
