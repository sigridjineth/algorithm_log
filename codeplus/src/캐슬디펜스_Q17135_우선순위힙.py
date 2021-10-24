from copy import deepcopy
from itertools import combinations
from heapq import heappop, heappush

n, m, d = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
castle_position = [i for i in range(m)]
gungsu_cases = tuple(combinations(castle_position, 3))

def get_enemy_count(arr):
    count = 0
    for i in range(n):
        for j in range(m):
            if (arr[i][j] == 1):
                count += 1
    return count

def attack_enemy(index, arr):
    remove_list = []
    attacked = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    for gungsu_position in gungsu_cases[index]: # gungsu_position은 열만 달라지고 행은 동일하다
        pq = []
        for i in range(n-1, -1, -1):
            for j in range(m):
                if (arr[i][j] == 1):
                    diff = abs(n - i) + abs(gungsu_position - j)
                    if (diff <= d):
                        # 우선순위 힙을 이용하여 diff가 가장 큰 것부터 꺼내올 수 있도록 한다
                        heappush(pq, [diff, j, i])
        if (pq):
            diff, x, y = heappop(pq)
            remove_list.append([y, x])
            
    for (y, x) in remove_list:
        if not attacked[y][x]: # 중복 제거 문제를 해결하기 위하여 새로운 boolean 배열을 만들어 해결한다
            attacked[y][x] = True
            count += 1
            arr[y][x] = 0
    return count

def move_enemy(arr):
    arr[-1] = [0 for _ in range(m)]
    for i in range(-1, -n, -1):
        arr[i] = arr[i-1]
    arr[0] = [0 for _ in range(m)]

def simulation(gungsu_cases_idx, arr):
    count = 0
    while (get_enemy_count(arr) != 0):
        count = count + attack_enemy(gungsu_cases_idx, arr)
        move_enemy(arr)
    return count

def solution():
    answer = 0
    for i in range(len(gungsu_cases)):
        a = deepcopy(b)
        count = simulation(i, a)
        if (answer < count):
            answer = count
    return answer

print(solution())
