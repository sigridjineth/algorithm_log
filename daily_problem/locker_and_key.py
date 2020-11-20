# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행
    m = len(a[0]) # 열
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][(n-i)-1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock)
    for i in range(lock_length, lock_length * 2:
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)
    # 자물쇠의 크기를 기존의 3배로 변환. 완전 탐색을 수월하게 하기 위해서 리스트 크기를 3배로 변환하여 새 리스트 만든다
    new_lock = [[0] * (lock_length * 3) for _ in range(lock_length * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(lock_length):
        for j in range(lock_length):
            new_lock[i+lock_length][j+lock_length] = lock[i][j]
    # 4가지 방향에 대하여 확인
    for rotation in range(4):
        # 열쇠 회전
        key = rotate_a_matrix_by_90_degree(key)
        # 기존 자물쇠에 2배까지일 때만 체크하는데, 그 이유는 기존 자물쇠에 key_length 만을 더해주기 때문이다.
        # 만약 3배까지로 체크하면 신규 자물쇠를 넘어서게 된다.
        for x in range(lock_length * 2):
            for y in range(lock_length * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(key_length):
                    for j in range(key_length):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if (check(new_lock) == True):
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for k in range(key_length):
                    for i in range(key_length):
                        new_lock[x+k][y+i] -= key[k][i]