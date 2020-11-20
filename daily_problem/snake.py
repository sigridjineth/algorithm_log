# 뱀 백준 3190번
print('snake prob.')
n = int(input()) # 보드의 크기
k = int(input()) # 사과의 크기
data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보. x, y를 (1, 1)로 초기화할 것이므로 1~n까지 생성한다.
info = [] # 방향 회전 정보

# 맵 정보에 사과를 업데이트한다.
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 오른쪽 기준 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    # 뱀이 존재하는 위치
    x, y = 1, 1
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 오른쪽
    time = 0 # 시작 후 지난 초 시간
    index = 0 # 회전 정보
    q = [(x, y)] # 뱀의 차지 위치

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if (nx >= 1 and nx <= n and ny >= 1 and ny <= n and data[nx][ny] != 2):
            # 사과가 없다면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                # 새로운 뱀의 위치를 그래프에 추가
                data[nx][ny] = 2
                q.append((nx, ny))
                # 기존 뱀의 위치를 그래프에 제거
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후 꼬리 잔류
            if data[nx][ny] == 1:
                # 새로운 뱀의 머리 위치를 그래프에 표시
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 자기 자신의 몸통에 부딪힌 경우
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1
        if (time == info[index][0]):
            direction = turn(direction, info[index][1])
            index += 1
                
    return time

print(simulate())