def solution(m, n, board):
    board = [list(x) for x in board]
    matched = True
    while (matched):
        # 1단계: 일치 여부 찾기
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if (board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != '#'):
                    matched.append((i, j))
        for (i, j) in matched:
            board[i][j] = board[i + 1][j] = board[i][j + 1] = board[i + 1][j + 1] = '#'
        for i in range(1, m):
            for j in range(n):
                if (board[i][j] == '#'):
                    board[i][j], board[i - 1][j] = board[i - 1][j], '#'
    count = 0
    for x in board:
        count += x.count('#')
    return count
