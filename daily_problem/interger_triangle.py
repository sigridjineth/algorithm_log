# 정수 삼각형
def solution():
    n = int(input())
    dp = []
    for _ in range(n):
        dp.append(list(map(int, input().split())))
    # 다이나믹 프로그래밍으로 두 번째 줄부터 탐색하며 위를 참조하면서 값을 변경해간다
    for i in range(1, n):
        for j in range(0, i+1):
            # 왼쪽 대각선 위에서 올라오는 경우
            if (j==0):
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            dp[i][j] = dp[i][j] + max(left_up, up)

    return max(dp[i-1])