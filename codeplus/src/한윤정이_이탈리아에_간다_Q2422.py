def solution():
  n, m = map(int, input().split())
  a = [[False] * (n + 1) for _ in range(n + 1)]

  for _ in range(m):
    u, v = map(int, input().split())
    a[u][v] = True
    a[v][u] = True

  answer = 0

  for i in range(1, n - 1):
    for j in range(i + 1, n):
      for k in range(j + 1, n + 1):
        if (a[i][j] or a[i][k] or a[j][k]):
          continue
        answer += 1
  
  return answer

print(solution())
