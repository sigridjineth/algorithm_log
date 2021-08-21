def solution():
  n = int(input())
  m = list(map(int, input().split()))
  answer = None

  if (n == 1):
    return 0

  def check(diff1, diff2):
    change = 0
    if (diff1 != 0):
      change += 1
    if (diff2 != 0):
      change += 1

    diff = (m[1] + diff2) - (m[0] + diff1)
    now = (m[1] + diff2) + diff

    for k in range(2, n):
      if (m[k] == now):
        now = m[k] + diff
        continue
      elif (m[k] - 1 == now):
        now = (m[k] - 1) + diff
        change += 1
        continue
      elif (m[k] + 1 == now):
        now = (m[k] + 1) + diff
        change += 1
        continue
      else:
        return None
    return change

  for i in range(-1, 2):
    for j in range(-1, 2):
      temp = check(i, j)
      if (check(i, j) == None):
        continue
      if (answer == None or answer > temp):
        answer = temp
  
  if (answer == None):
    answer = -1

  return answer

print(solution())
