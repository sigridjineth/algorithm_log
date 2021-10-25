def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    select, c = [0 for _ in range(9)], [0 for _ in range(9)]
    # 3번 타자가 처음, c에 체크했다고 하고 select에 해당 타자번호 입력
    select[3] = 0
    c[3] = True
    answer = 0

    # 타순 구하고 -> cnt가 9이면 시뮬레이션 동작 -> 이닝 전체별로
    def dfs(count):
        nonlocal answer
        if (count == 9): # 일단 9번 타자까지 오면 점수를 계산하고 다시 돌린다
            hitter_current, score = 0, 0
            for inning in a:
                out, base1, base2, base3 = 0, 0, 0, 0
                while (out <= 2):
                    hitter_num = select[hitter_current]
                    point = inning[hitter_num]
                    if (point == 0):
                        out += 1
                    elif (point == 1):
                        score = score + base3
                        base1, base2, base3 = 1, base1, base2
                    elif (point == 2):
                        score = score + (base2 + base3)
                        base1, base2, base3 = 0, 1, base1
                    elif (point == 3):
                        score = score + (base1 + base2 + base3)
                        base1, base2, base3 = 0, 0, 1
                    else: # 홈런
                        score = score + (base1 + base2 + base3 + 1)
                        base1, base2, base3 = 0, 0, 0
                    hitter_current += 1
                    hitter_current %= 9
            answer = max(score, answer)
            return
        # 타순 정하기는 전형적인 DFS 방식을 이용한다!
        for i in range(9):
            if (c[i] is True): continue
            # c[i]; i번째 선수는 이미 정해졌다
            c[i] = True
            # select[i] = count; 타자 번호 i가 count 번째로 치는 선수이다
            select[i] = count
            dfs(count + 1)
            c[i] = False
            select[i] = 0
    
    dfs(1)
    return answer

print(solution())
