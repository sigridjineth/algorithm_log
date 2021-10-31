from collections import deque

dx = [0, 1]
dy = [1, 0]

def solution(board):
    isZero = False
    q = deque()
    # to check "믿음으로 갈 수 있나?"
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == 0):
                isZero = True
                break
    
    def BFS(board):
        # score를 board 첫 칸에 다 몰아줄 것이다
        score = board[0][0]
        while (len(q) > 0):
            count_vertical = 0
            count_horizontal = 0
            [x, y] = q.popleft()
            nx = x + dx[0]
            ny = y + dy[0]
            if (nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board)):
                count_vertical = board[ny][nx]
                # zero를 greedy하게 찾는다; when currently considering minus score
                if (count_vertical == 0 and score < 0):
                    score = abs(score)
                    q.append([nx, ny])
                    continue
            nx_right = x + dx[1]
            ny_right = y + dy[1]
            if (nx_right >= 0 and ny_right >= 0 and nx_right < len(board) and ny_right < len(board)):
                count_horizontal = board[ny_right][nx_right]
                if (count_horizontal == 0 and score < 0):
                    score = abs(score)
                    q.append([nx_right, ny_right])
                    continue
            if (isZero == True and abs(score + count_vertical) < abs(score + count_horizontal)):
                q.append([nx_right, ny_right])
                score += count_horizontal
            elif (isZero == True and abs(score + count_vertical) > abs(score + count_horizontal)):
                q.append([nx, ny])
                score += count_vertical
            elif (isZero == False and count_vertical < count_horizontal):
                q.append([nx_right, ny_right])
                score += count_horizontal
            elif (isZero == False and count_vertical > count_horizontal):
                q.append([nx, ny])
                score += count_vertical
        return score
    
    q.append([0, 0])
    answer = BFS(board)
    return answer

board = [[-10, 20, 30], [-10, 0, 10], [-20, 40, 1]]
board2 = [[1, -7, 2, 1, -1], [2, 3, 0, -1, -2], [1, -1, 6, -1, -2], [-1, 1, -2, 0, 4], [-10, 5, -3, -1, 1]]
print(solution(board))
print(solution(board2))
