# 곱하기 혹은 더하기
data = input()
result = int(data[0])

for i in range(1, len(data)):
    # 다음 문자 또는 이전 문자가 0이나 1인지 확인
    next = int(data[i])
    if (next <=1 or result <=1):
        result += next
    else:
        result *= next

print(result)
