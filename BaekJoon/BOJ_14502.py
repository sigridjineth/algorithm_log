import copy
import sys
 
input = sys.stdin.readline
 
N, M = map(int, input().strip().split())
NM = []
for i in range(N):
    L = list(map(int, input().strip().split()))
    NM.append(L)
 
dr = [-1,0,1,0] # 위아래 row 단위로 이동
dc = [0,1,0,-1] # 좌우 column 단위로 이동
max_value = 0 # clean 지역의 개수를 return 하기 위한 변수
virus_list = [] # 바이러스 리스트 만들기
for i in range(N):
    for j in range(M):
        if NM[i][j] == 2:
            virus_list.append([i,j])
 
# 벽 선택하기
def select_wall(start,count):
    global max_value
    if count == 3 : # 종료조건, 벽 3개 선택 완료
        sel_NM = copy.deepcopy(NM) # deepcopy로 벽이 선택된 배열 복사
        for num in range(len(virus_list)):
            r, c = virus_list[num]
            spread_virus(r, c, sel_NM)
        safe_counts = sum(i.count(0) for i in sel_NM) # clean 지역 count
        max_value = max(max_value, safe_counts)
        return True
    else:
        for i in range(start, N*M): # 2차원 배열에서 조합 구하기
            r = i // M
            c = i % M
            if NM[r][c] == 0 : # 안전영역인 경우 벽으로 선택가능
                NM[r][c] = 1 # 벽으로 변경
                select_wall(i,count+1) # 벽선택
                NM[r][c] = 0
 
 
def spread_virus(r,c,sel_NM):
    if sel_NM[r][c] == 2:
        # 상하좌우 4방향을 확인하고 범위를 벗어나거나, 벽을 만날때까지 반복
        for dir in range(4):
            n_r = r+dr[dir]
            n_c = c+dc[dir]
            if n_r >= 0 and n_c >=0 and n_r < N and n_c < M : # 범위를 벗어나지 않을때
                if sel_NM[n_r][n_c] == 0 :
                    sel_NM[n_r][n_c] = 2
                    spread_virus(n_r,n_c,sel_NM)

select_wall(0,0)
print(max_value)