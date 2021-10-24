import copy
n, m, d = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

def calc(gungsu_1, gungsu_2, gungsu_3):
    a = copy.deepcopy(b)
    answer = 0
    while True: # one turn
    # To end this game, all enemy should be eliminate
        enemy_total = 0
        for i in range(n):
            for j in range(m):
                enemy_total = enemy_total + a[i][j]
        if (enemy_total == 0):
            break
        gungsus = [gungsu_1, gungsu_2, gungsu_3]
        now_attacking = [(-1, -1)] * 3
        for gungsu in range(3):
            rx = n # static row
            ry = gungsus[gungsu] # dynamic column
            x, y, dist = -1, -1, -1
            for j in range(m): # starting from the column to reduce unnecessary checking code
                for i in range(n):
                    if (a[i][j] == 1): # if not being enemy
                        dx = abs(rx - i)
                        dy = abs(ry - j)
                        dd = dx + dy
                        if (dd <= d): # if within threshold
                            if (dist == -1 or dist > dd):
                                x = i
                                y = j
                                dist = dd
            now_attacking[gungsu] = (x, y)
        # the reason for recording all gungsu's attacking position is to avoid duplicate counting of removing enemies
        for (x, y) in now_attacking:
            if (x == -1 or y == -1): continue
            if (a[x][y] != 0): answer = answer + 1
            a[x][y] = 0
        # moving enemies from the bottom (accepting enemies from the bottom)
        for i in range(n-1, -1, -1):
            for j in range(m):
                if (i == 0): # exception at the beginning row
                    a[i][j] = 0
                else:
                    a[i][j] = a[i-1][j]
    
    return answer


def solution():
    answer = 0
    for gungsu_1 in range(m):
        for gungsu_2 in range(gungsu_1 + 1, m):
            for gungsu_3 in range(gungsu_2 + 1, m):
                candidate = calc(gungsu_1, gungsu_2, gungsu_3)
                if (answer < candidate):
                    answer = candidate
    return answer

print(solution())
