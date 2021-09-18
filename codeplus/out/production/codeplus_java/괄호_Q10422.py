def first_dynamics():
  mod = 1000000007
  d = [-1] * 5001
  
  def go(n):
      if n == 0:
          return 1
      if d[n] >= 0:
          return d[n]
      d[n] = 0
      for i in range(2, n+1, 2):
          d[n] += go(i-2) * go(n-i)
          d[n] %= mod
      return d[n]

  t = int(input())
  for _ in range(t):
      n = int(input())
      if n%2 == 0:
          print(go(n))
      else:
          print(0)

def second_dynamics():
  mod = 1000000007
  d = [[0] * 5001 for _ in range(5001)]
  d[0][0] = 1
  for i in range(1, 5001):
      for j in range(i+1):
          if j+1 <= i:
              d[i][j] += d[i-1][j+1]
          if j-1 >= 0:
              d[i][j] += d[i-1][j-1]
          d[i][j] %= mod
  t = int(input())
  for _ in range(t):
      n = int(input())
      print(d[n][0])
