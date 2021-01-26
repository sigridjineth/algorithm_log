from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

def solution(n, m, city):
    chicken = []
    home = []
    chicken_distance = []
    answer = 20210101

    for i in range(n):
        for j in range(n):
            if (city[i][j] == 2):
                chicken.append((i, j))
            elif (city[i][j] == 1):
                home.append((i, j))

    for i, (hi, hj) in enumerate(home):
        chicken_distance.append([0] * len(chicken)) # 치킨집 개수 만큼 추가
        for j, (ci, cj) in enumerate(chicken):
            chicken_distance[i][j] = abs(ci-hi) + abs(cj-hj)
    
    if (len(chicken) <= m):
        return sum(map(lambda x: min(x), chicken_distance))
    
    chicken_index = combinations(range(len(chicken)), m)

    for ci in chicken_index:
        distance = 0
        for h in range(len(home)):
            temp = 20210101
            for i in ci:
                temp = min(temp, chicken_distance[h][i])
            distance += temp
        answer = min(answer, distance)

    return answer

print(solution(n, m, city))
