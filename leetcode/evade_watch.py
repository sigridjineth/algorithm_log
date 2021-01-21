# 감시 피하기
import copy

n = int(input()) # 복도의 크기
board = [] # 복도 정보
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보
directions = ['LEFT', 'RIGHT', 'UP', 'DOWN'] # 이동 가능한 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치를 저장
        if (board[i][j] == 'T'):
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 빈 공간 위치 지정
        if (board[i][j] == 'O'):
            spaces.append((i, j))

# 특정 방향으로 감시를 진행하여, 학생을 발견하면 True 이고 발견하지 못하면 False
def watch(x, y, direction):
    # 왼쪽으로 감시
    if (direction == 'LEFT'):
        while (y>=0):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            y -= 1
    # 오른쪽으로 감시
    if (direction == 'RIGHT'):
        while (y<n):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            y += 1
    # 위쪽으로 감시
    if (direction == 'UP'):
        while (x>=0):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            x -= 1
    # 아래쪽으로 감시
    if (direction == 'DOWN'):
        while (x<n):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            x += 1
    return False

# 장애물을 설치하고 한 명이라도 학생이 감지되는지 검사
def detect():
    count = 0
    # 모든 선생님의 위치를 확인
    for x, y in teachers:
        for direction in directions:
            if (watch(x, y, direction) == True):
                return True
            else:
                continue
        count += 1
    return False

check = False

def dfs(spaces, count):
    global check
    if (count == 3):
        if (detect() == False):
            check = True
        return
    for i, j in spaces: # 장애물 설치해보기
        board[i][j] = 'O'
        count += 1
        temp = copy.deepcopy(spaces)
        temp.remove((i, j))
        dfs(temp, count)

        board[i][j] == 'X' # 장애물 삭제하기
        count -= 1

dfs(spaces, 0)
if (check == True):
    print('YES')
else:
    print('NO')