# 공유기 설치: 자연수 분할 이용
def divide(target):
    divide_list = []
    for i in range(1, target//2+1):
        divide_list.append((i, target-i))
    return divide_list

def find_available(divide_list, houses_location):
    answer = 0
    for i in range(len(divide_list), 0, -1):
        x, y = divide_list[i-1][0], divide_list[i-1][1]
        count = 0
        for j in range(0, len(houses_location)):
            now = houses_location[j]
            for k in range(j+1, len(houses_location)):
                next2 = houses_location[k]
                if (count == 0) and (abs(next2-now) == x):
                    count += 1
                elif (count == 1) and (abs(next2-now) == y):
                    count += 1
                elif (count == 2):
                    answer = max(answer, x)
                    break
    return answer

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

divide_list = divide(abs(data[-1] - data[0]))
answer = find_available(divide_list, data)
print(answer)