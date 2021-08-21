def solution():
  n, m = map(int, input().split())
  a = [list(map(int, input().split())) for _ in range(n)]
  cctv = []

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  
  for i in range(n):
    for j in range(m):
      # cctv를 탐색해서 별도의 배열에 추가해준다.
      if (1 <= a[i][j] <= 5):
        cctv.append((a[i][j], i, j))

  def transmit_cctv(a, b, x, y, dir):
    n = len(a)
    m = len(a[0])
    i, j = x, y

    while True:
      if (i < 0 or i >= n or j < 0 or j >= m):
        break
      if (a[i][j] == 6):
        break
      b[i][j] = a[x][y]
      i += dx[dir]
      j += dy[dir]
  
  def dfs(a, cctv, index, dirs):
     # index번째 CCTV의 모든 방향을 가리킬 수 있는 경우의 수의 모든 조합을 구한다.
    if (len(cctv) != index):
      ans = None
      for i in range(4):
        temp = dfs(a, cctv, index + 1, dirs + [i])
        if (ans == None or ans > temp):
          ans = temp
      return ans

    elif (len(cctv) == index):
      n = len(a)
      m = len(a[0])
      b = [row[:] for row in a]

      for index, (num, x, y) in enumerate(cctv):
        # 각각의 CCTV에 따라 모두 감시중인 녀석들을 체크한다.
        if (num == 1):
          transmit_cctv(a, b, x, y, dirs[index])
        elif (num == 2):
          transmit_cctv(a, b, x, y, dirs[index])
          transmit_cctv(a, b, x, y, (dirs[index] + 2) % 4)
        elif (num == 3):
          transmit_cctv(a, b, x, y, dirs[index])
          transmit_cctv(a, b, x, y, (dirs[index] + 1) % 4)
        elif (num == 4):
          transmit_cctv(a, b, x, y, dirs[index])
          transmit_cctv(a, b, x, y, (dirs[index] + 1) % 4)
          transmit_cctv(a, b, x, y, (dirs[index] + 2) % 4)
        elif (num == 5):
          transmit_cctv(a, b, x, y, dirs[index])
          transmit_cctv(a, b, x, y, (dirs[index] + 1) % 4)
          transmit_cctv(a, b, x, y, (dirs[index] + 2) % 4)
          transmit_cctv(a, b, x, y, (dirs[index] + 3) % 4)

      count = 0
      for i in range(n):
        for j in range(m):
          if (b[i][j] == 0):
            count += 1
      return count

  return dfs(a, cctv, 0, [])

print(solution())
