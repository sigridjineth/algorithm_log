a = input()
b = input()
n = len(a)
m = len(b)
a = " " + a
b = " " + b
d = [[0]*(m+1) for _ in range(n+1)]
v = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            d[i][j] = d[i-1][j-1] + 1
            v[i][j] = 1
        else:
            if d[i-1][j] < d[i][j-1]:
                d[i][j] = d[i][j-1]
                v[i][j] = 2
            else:
                d[i][j] = d[i-1][j]
                v[i][j] = 3
print(d[n][m])
ans = ""
while n > 0 and m > 0:
    if v[n][m] == 1:
        ans += a[n]
        n -= 1
        m -= 1
    elif v[n][m] == 2:
        m -= 1
    else:
        n -= 1
print(ans[::-1])
