# 연산자 끼워넣기
n = int(input())
data = list(map(int, input().split()))
add, minus, multiply, divide = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global n, add, minus, multiply, divide, min_value, max_value
    # 모든 경우를 다 사용한 경우
    if (i == n):
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if (add != 0):
            add -= 1
            dfs(i+1, now + data[i]) # 다음 순서가 무엇이고 이전 순서가 무엇인지 생각할 것
            add += 1
        if (minus != 0):
            minus -= 1
            dfs(i+1, now - data[i])
            minus += 1
        if (multiply != 0):
            multiply -= 1
            dfs(i+1, now * data[i])
            multiply += 1
        if (divide != 0):
            divide -= 1
            dfs(i+1, now // data[i])
            divide += 1

dfs(i, data[0])
print(min_value)
print(max_value)