print("n을 입력")
n = int(input()) #첫 줄에는 1에서 n까지 간다는 사실을 통지한다
count = 1
stack = []
result = []

for i in range(1, n+1):
    inputNum = int(input()) #데이터 횟수만큼 반복하여 받습니다.
    if count <= inputNum:
        while count <= inputNum:
            stack.append(count)
            count += 1
            result.append("+")
        stack.pop()
        result.append("-")
        print(result)
        continue
    if stack[-1] == inputNum:
        stack.pop()
        result.append("-")
        print(result)
        continue
    else:
        result.append("NO")
        print(result)
        exit(0)