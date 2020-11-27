# 퇴사 백준 14501번
def solution():
    n = int(input())
    data = []
    for _ in range(n):
        t, p = map(int, input().split())
        data.append((t, p))
    dp = [0]*(n+1)
    answer = 0

    # 뒤에서부터 하나씩 확인해서 올라올 것. 그러면 최종적으로 처음에 누적된 DP를 바탕으로 시작점에서 방향을 알 수 있다
    for i in range(n-1, -1, -1):
        time = data[i][0]+i
        if (time <= n):
            dp[i] = max(data[i][1] + dp[time], answer)
            answer = dp[i]
        else:
            dp[i] = answer
    
    return answer