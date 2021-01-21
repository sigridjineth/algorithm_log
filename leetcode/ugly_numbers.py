# 못생긴 수 Google Interview
def solution():
    n = int(input())
    dp = [0]*n # 못생긴 수를 담는 dp 테이블
    dp[0] = 1 # 1은 못생긴 수로 간주

    index2, index3, index5 = 0, 0, 0
    next2, next3, next5 = 2, 3, 5

    for i in range(1, n):
        # 2를 곱한 것과 3을 곱한 것과 5를 곱한 것 중에서 어느 것이 더 작은 지를 고민해볼 것
        dp[i] = min(next2, next3, next5)
        
        if (dp[i] == next2):
            index2 += 1
            next2 = dp[index2] * 2

        if (dp[i] == next3):
            index3 += 1
            next3 = dp[index3] * 2
        
        if (dp[i] == next5):
            index5 += 1
            next5 = dp[index5] * 2

    return dp[n-1]
