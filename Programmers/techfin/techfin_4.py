def turn(d):
    return (d + 1) % 4

dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]

def solution(n, jump):
    board = [[0] * n for _ in range(n)]
    chk_board = [[False] * n for _ in range(n)]
    chk_board[0][0] = True
    d = r = c = 0
    board[r][c] = 1
    i = 2
    j = 0
    answer = [0, 0]
    while i <= n * n:
        if j == jump:
            board[r][c] = i
            if i == n * n:
                answer[0] = r + 1
                answer[1] = c + 1
            i += 1
            j = 0
        if n % 2 == 1 and r == n // 2 and c == n // 2:
            r = 0
            c = -1
            d = 0
            chk_board = [[False] * n for _ in range(n)]
        elif n % 2 == 0 and r == n // 2 and c == n // 2 - 1:
            r = 0
            c = -1
            d = 0
            chk_board = [[False] * n for _ in range(n)]

        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            if chk_board[nr][nc]:
                d = turn(d)
            else:
                chk_board[nr][nc] = True
                if board[nr][nc]:
                    r, c = nr, nc
                    continue
                else:
                    j += 1
                r, c = nr, nc
        else:
            d = turn(d)
    return answer

print(solution(5, 3))
print(solution(4, 1))
print(solution(3, 10))
print(solution(25, 1))
