# 럭키 스트레이트
n = input()
count = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(len(n) // 2):
    count += int(n[i])

# 오른쪽 부분의 자릿수 합 더하기
for i in range(len(n) // 2, len(n)):
    count -= int(n[i])

# 왼쪽 부분과 오른쪽 부분이 동일한 지 검사
if count == 0:
    print('LUCKY')
else:
    print('READY')