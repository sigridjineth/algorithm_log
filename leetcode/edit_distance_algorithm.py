def edit_distance(string1, string2):
    n = len(string1)
    m = len(string2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    # dp 테이블 초기 설정
    for i in range(1, n+1):
        # 처음에는 공집합이다.
        dp[i][0] = i # 맨 처음 행 또는 열에는 하나씩 추가해주는 것으로 한다.
    for j in range(1, m+1):
        dp[0][j] = j # 여기도 마찬가지이다.
    
    # 최소 편집 거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입한다.
            if (string1[i-1] == string2[j-1]):
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면, 세 가지 경우 중에서 최소값을 찾아 대입한다.
            # 오른쪽으로 가면 삽입, 대각선에서 내려오면 편집, 위에서 내려오면 삭제
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

    return dp[n][m]

def solution():
    string1 = input()
    string2 = input()
    
    return edit_distance(string1, string2)