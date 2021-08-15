a = input()
b = input()
n = len(a)
m = len(b)
a = " " + a
b = " " + b
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = 0
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if ans < d[i][j]:
            ans = d[i][j]
print(ans)