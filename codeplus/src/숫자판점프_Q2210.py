def solution():
  n = 5
  a = [list(map(int, input().split())) for _ in range(n)]
  answer = set()

  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  
  def go(x, y, num, length):
    if (length == 6):
      answer.add(num)
      return
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if (0 <= nx < n and 0 <= ny < n):
        go(nx, ny, str(num) + str(a[nx][ny]), length + 1)

  for i in range(n):
    for j in range(n):
      go(i, j, a[i][j], 1)
    
  return len(answer)

print(solution())
