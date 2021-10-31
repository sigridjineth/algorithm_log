dr = [0, 1]  # 우 하
dc = [1, 0]

answer = 0


def dfs(row, col, value, n, board):
    global answer
    if row == n - 1 and col == n - 1:
        if answer < value:
            answer = value
        return

    for d in range(2):
        nr = row + dr[d]
        nc = col + dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] != 0:
                dfs(nr, nc, value + board[nr][nc], n, board)
            else:
                dfs(nr, nc, value, n, board)
                dfs(nr, nc, -value, n, board)


def solution(board):
    global answer
    n = len(board)
    dfs(0, 0, board[0][0], n, board)
    return answer
