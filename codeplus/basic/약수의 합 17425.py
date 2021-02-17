# 백준 약수의 합 17425

def solution():
    # 모든 경우의 수를 다 구할 것
    MAX = 1000000
    d = [1]*(MAX+1)
    s = [0]*(MAX+1)

    for i in range(2, MAX+1):
        j = 1
        while (i*j <= MAX):
            d[i*j] += i # 하나씩 순회하면서 경우에 해당하는 원소를 추가하기
            j += 1 # i * j가 MAX를 넘어가는 순간 문제의 조건을 벗어나므로, 그 이전까지 j를 하나씩 늘린다.
    
    for i in range(1, MAX+1):
        s[i] = s[i-1] + d[i] # x보다 작거나 같은 모든 자연수의 f(i) 값을 구한 것이다.
    
    t = int(input())
    answer = []
    for _ in range(t):
        n = int(input())
        answer.append(s[n])
    
    print('\n'.join(map(str, answer)) + '\n')

solution()