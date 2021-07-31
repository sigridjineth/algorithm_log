from collections import deque

def solution():
  dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
  dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]
  n = 8
  a = [input() for _ in range(n)]
  queue = deque()
  check = [[[False] * (n + 1) for j in range(n)] for i in range(n)]
  check[7][0][0] = True # 7행 0열부터 시작함
  queue.append((7, 0, 0))
  answer = False

  while queue:
    x, y, t = queue.popleft()
    if (x == 0 and y == 7): # 0행 7열이 되면 True가 되는 기저 조건
      answer = True
      break
    for k in range(9):
      nx, ny = x + dx[k], y + dy[k]
      nt = min(t + 1, 8)
      if (0 <= nx < n and 0 <= ny < n):
        if (nx - t >= 0 and a[nx - t][ny] == '#'): # 현재 벽 여부 확인
          continue
        if (nx - t >= 0 and a[nx - (t + 1)][ny] == '#'): # 1초 뒤에 내려오는 벽 여부 확인
          continue
        if (check[nx][ny][nt] == False): # 방문한 적이 없는 위치 확인
          check[nx][ny][nt] = True
          queue.append((nx, ny, nt))

  return (1 if answer else 0)

print(solution())
