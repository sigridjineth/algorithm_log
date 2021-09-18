def solution_bitmask():
  n, m = map(int, input().split())
  a = [list(map(int, input().split())) for _ in range(n)]
  house = []
  chicken_store = []
  answer = None
  
  for i in range(n):
    for j in range(n):
      if (a[i][j] == 1):
        house.append((i, j))
      elif (a[i][j] == 2):
        chicken_store.append((i, j))

  for i in range(1 << len(chicken_store)):
    count = bin(i).count("1")
    if (count > m):
      continue
    if (count == 0):
      continue
    else:
      case_distances = 0
      for j in range(len(house)):
        house_distances = None
        for k in range(len(chicken_store)):
          if (i & (1 << k) > 0):
            temp_x = abs(chicken_store[k][0] - house[j][0])
            temp_y = abs(chicken_store[k][1] - house[j][1])
            temp_d = temp_x + temp_y
            if (house_distances == None or house_distances > temp_d):
              house_distances = temp_d
        case_distances += house_distances
      if (answer == None or answer > case_distances):
        answer = case_distances
  
  return answer

from itertools import combinations

def solution_combinations():
  n, m = map(int, input().split())
  a = [list(map(int, input().split())) for _ in range(n)]

  chicken_store = []
  house = []
  answer = None
  chicken_distance = []

  for i in range(n):
    for j in range(n):
        if (a[i][j] == 2):
          chicken_store.append((i, j))
        elif (a[i][j] == 1):
          house.append((i, j))

  for i, (house_x, house_y) in enumerate(house):
    chicken_distance.append([0] * len(chicken_store))
    for j, (chicken_x, chicken_y) in enumerate(chicken_store):
      chicken_distance[i][j] = abs(chicken_x - house_x) + abs(chicken_y - house_y)
  
  chicken_index = combinations(range(len(chicken_store)), m)

  for index in chicken_index:
    distance = 0
    for h in range(len(house)):
      temp = None
      for i in index:
        if (temp == None or temp > chicken_distance[h][i]):
          temp = chicken_distance[h][i]
      distance += temp
    if (answer == None or answer > distance):
      answer = distance

  return answer

import sys
answer = sys.maxsize

def solution_recursive():
  n, m = map(int, input().split())
  a = [list(map(int, input().split())) for _ in range(n)]

  chicken_store = []
  house = []

  for i in range(n):
    for j in range(n):
        if (a[i][j] == 2):
          chicken_store.append((i, j))
        elif (a[i][j] == 1):
          house.append((i, j))

  check = [False] * len(chicken_store)

  def dfs(count, index):
    global answer
    if (count == m): # 정답을 맞추는 경우
      case_answer = 0
      for i in range(len(house)):
        house_distance = sys.maxsize
        for j in range(len(chicken_store)):
          if (check[j] == False):
            continue
          temp_x = abs(house[i][0] - chicken_store[j][0])
          temp_y = abs(house[i][1] - chicken_store[j][1])
          temp_d = temp_x + temp_y
          house_distance = min(house_distance, temp_d)
        case_answer += house_distance
      answer = min(answer, case_answer)
      return

    if (index >= len(chicken_store)): # 정답을 구할 수 없는 경우
        return
    
    # 그 외의 경우
    check[index] = True
    dfs(count + 1, index + 1)

    check[index] = False
    dfs(count, index + 1)

  dfs(0, 0)
  
  return answer

print(solution())

