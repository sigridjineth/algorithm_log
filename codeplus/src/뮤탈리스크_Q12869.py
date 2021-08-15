def go(i, j, k, d):
  if (i < 0):
    return go(0, j, k, d)
  if (j < 0):
    return go(i, 0, k, d)
  if (k < 0):
    return go(i, j, 0, d)
  if (i == 0 and j == 0 and k == 0):
    return 0
  ans = d[i][j][k]
  if (ans != -1):
    return ans
  ans = 1000000
  if (ans > go(i - 1, j - 3, k - 9, d)):
    ans = go(i - 1, j - 3, k - 9, d)
  if (ans > go(i - 1, j - 9, k - 3, d)):
    ans = go(i - 1, j - 9, k - 3, d)
  if (ans > go(i - 3, j - 1, k - 9, d)):
    ans = go(i - 3, j - 1, k - 9, d)
  if (ans > go(i - 3, j - 9, k - 1, d)):
    ans = go(i - 3, j - 9, k - 1, d)
  if (ans > go(i - 9, j - 1, k - 3, d)):
    ans = go(i - 9, j - 1, k - 3, d)
  if (ans > go(i - 9, j - 3, k - 1, d)):
    ans = go(i - 9, j - 3, k - 1, d)
  ans += 1
  d[i][j][k] = ans
  return d[i][j][k]

def solution():
  n = int(input())
  scv = list(map(int, input().split()))
  while (len(scv) < 3):
    scv += [0]
  d = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
  return go(scv[0], scv[1], scv[2], d)

print(solution())
