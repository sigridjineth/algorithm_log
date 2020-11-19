# 데이터 뒤집기 백준 1439번
data = input()
one_to_zero = 0
zero_to_one = 0

# 첫 번째 원소에 대하여 우선 처리
if (data[0] == '1'):
    one_to_zero += 1
else:
    zero_to_one += 1

# 두 번째 원소부터는 모든 원소를 확인한다
for i in range(0, len(data) - 1):
    if (data[i] != data[i+1]):
        # 다음 번에 1에서 0으로 바뀌는 경우 더하기
        if (data[i+1] == '1'):
            one_to_zero += 1
        # 다음 번에 0에서 1로 바뀌는 경우 더하기
        else:
            zero_to_one += 1

print(min(one_to_zero, zero_to_one))
