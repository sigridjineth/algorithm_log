def solution():
  n = int(input())
  a = list(input())
  for i in range(0, n, 2): # 숫자의 형 변환
    a[i] = int(a[i])
  m = (n - 1) // 2 # 연산자의 개수 
  ans = None

  # 비트마스크를 이용하여 연산자의 부분집합을 구한다
  for s in range(1 << m):
    ok = True
    for i in range(m - 1): # 연속인 경우 제외한다
      if ((s & (1 << i)) > 0 and (s & (1 << (i + 1))) > 0):
        ok = False
    if (ok == False):
      continue
    b = a[:] # hard copy
    for i in range(m):
      if (s & (1 << i) > 0): # 괄호 우선 선택된 경우
        k = 2 * i + 1
        if (b[k] == "+"):
          b[k - 1] += b[k + 1]
          b[k] = "+"
          b[k + 1] = 0
        if (b[k] == "-"):
          b[k - 1] -= b[k + 1]
          b[k] = "+"
          b[k + 1] = 0
        if (b[k] == "*"):
          b[k - 1] *= b[k + 1]
          b[k] = "+"
          b[k + 1] = 0

    temp = b[0] # 계산 시작
    for i in range(m):
      k = 2 * i + 1
      if (b[k] == "+"):
        temp += b[k + 1]
      elif (b[k] == "-"):
        temp -= b[k + 1]
      elif (b[k] == "*"):
        temp *= b[k + 1]
    if (ans == None or ans < temp):
      ans = temp
  
  return ans

print(solution())
