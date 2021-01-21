# 병사 배치하기 백준 18353번
# LIS로 풀이한다! 부분수열의 길이를 구한다.
def solution():
    n = int(input())
    array = list(map(int, input().split()))
    array.reverse() # 가장 긴 증가하는 부분수열 문제로 바꾸자
    dp = [1] * n # 최소 하나의 길이를 갖는다

    for i in range(n): # array[i]가 마지막일 때
        for j in range(0, i): # 0보다 크고 i보다 작은 것들 중에서
            if (array[j] < array[i]): # i가 마지막 항이 가능한 경우
                dp[i] = max(dp[i], dp[j] + 1) # 현재길이와 이전길이 + 1 중에서 더 큰 것을 선택한다.

    return n - max(dp)