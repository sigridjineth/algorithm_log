def solution():
  n, m = map(int, input().split())
  a = [[False] * (m + 1) for _ in range(n + 1)]
  friends_num = [0] * (n + 1)

  for _ in range(m):
    u, v = map(int, input().split())
    a[u][v] = a[v][u] = True
    friends_num[v] += 1
    friends_num[u] += 1
  
  answer = None

  for i in range(1, n + 1):
    for j in range(2, n + 1):
      if (a[i][j] == True):
        for k in range(3, n + 1):
          if (a[i][k] and a[j][k]):
            temp = (friends_num[i] - 2) + (friends_num[j] - 2) + (friends_num[k] - 2)
            if (answer == None or answer > temp):
              answer = temp
  
  if (answer == None):
    answer = -1

  return answer

print(solution())
