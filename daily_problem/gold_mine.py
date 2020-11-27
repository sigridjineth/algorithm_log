# 금광
def solution():
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    dp = []
    index = 0

    for i in range(n):
        dp.append(temp[index:index+m])
        index += m # 어짜피 맨 처음의 열에는 원래 데이터가 보존되어야 하므로, 바로 DP에 넣어버린다.
    
    for i in range(1, m):
        for j in range(n):
            # 왼쪽 위에서 오는 경우
            if (j == 0):
                left_up = 0 # 끝점에서 더 위를 보는 것은 범위를 벗어나므로 없는 것 처리
            else:
                left_up = dp[j-1][i-1]

            # 왼쪽 아래에서 오는 경우
            if (j == n-1):
                left_down = 0 # 끝점에서 더 아래를 보는 것은 범위를 벗어나므로 없는 것 처리
            else:
                left_down = dp[j+1][i-1]

            # 왼쪽에서 오는 경우
            if (j == 0):
                left = 0 # 끝점에서 더 왼쪽으로 보는 것은 범위를 벗어나므로 없는 것 처리
            else:
                left = dp[j][i-1]
                
            dp[j][i] = dp[j][i] + max(left_up, left_down, left)
    
    result = 0
    for a in range(n):
        result = max(result, dp[a][m-1])
    return result