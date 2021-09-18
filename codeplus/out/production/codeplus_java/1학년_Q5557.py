n = int(input())-1
a = list(map(int,input().split()))
goal = a[-1]
a = a[:-1]
d = [[0]*21 for _ in range(n)]
d[0][a[0]] = 1
for i in range(1,n):
    for j in range(21):
        if j-a[i] >= 0:
            d[i][j] += d[i-1][j-a[i]]
        if j+a[i] <= 20:
            d[i][j] += d[i-1][j+a[i]]
print(d[n-1][goal])