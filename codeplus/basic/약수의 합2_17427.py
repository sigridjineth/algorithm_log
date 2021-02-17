# 백준 약수의 합 2 17427
def solution():
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        answer += (n//i) * i # 배수의 아이디어를 이용한다
    return answer

print(solution())