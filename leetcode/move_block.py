from collections import deque

def solution(board):
    # 맵의 외곽에 벽을 설치하는 형태로 맵 변형
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)] # n * n에서 (n+1) * (n+1)로 늘어남
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1,1), (1,2)} # 튜플로 위치정보 처리
    visited.append((pos, 0)) # 시작점은 항상 0초로 처리하며, 방문처리

    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # 만약 (N, N) 이라면 최단거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치서 이동 가능한 위치 반환
        for next_position in get_next_position(position, new_board):
            if (next_position not in visited):
                q.append((next_position, cost+1))
                visited.append(next_position)
    # 만약에 return을 위의 (N, N)의 경우에서 없었다면 0을 반환
    return 0

def get_next_position(position, board):
    # 이동가능한 위치들인 반환 결과
    next_position = []
    position = list(position) # 위치 정보가 집합으로 표현되어 있는데, 이를 리스트 정보로 변환함

    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상하좌우 표현
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_x = pos1_x + dx[i]
        pos1_y = pos1_y + dy[i]
        pos2_x = pos2_x + dx[i]
        pos2_y = pos2_y + dy[i]

        # 두 칸이 모두 비어있는 경우 그냥 이동 가능하다
        if (board[pos1_x][pos1_y] == 0) and (board[pos2_x][pos2_y] == 0):
            next_position.append((pos1_x, pos1_y), (pos2_x, pos2_y))

        # 현재 로봇이 가로로 놓여있는 경우
        if (pos1_x == pos2_x):
            for i in [-1, 1]: # 위쪽으로 회전하거나 아래쪽으로 회전하거나
                if (board[pos1_x+i][pos1_y] == 0) and (board[pos2_x+i][pos2_y] == 0):
                    next_position.append((pos1_x, pos1_y), (pos2_x, pos2_y))

        # 현재 로봇이 세로로 놓여있는 경우
        elif (pos1_y == pos2_y):
            for i in [-1, 1]: # 왼쪽으로 회전하거나 오른쪽으로 회전해본다
                if (board[pos1_x][pos1_y+i] == 0) and (board[pos2_x][pos2_y+i] == 0):
                    # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                    next_position.append((pos1_x, pos1_y), (pos1_x, pos1_y+i))
                    next_position.append((pos2_x, pos2_y), (pos2_x, pos2_y+i))

    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_position