n = int(input())
array = list()

for _ in range(n): #배열에 숫자 넣기
    array.append(int(input()))

for i in range(n):
    for j in range(i+1, n):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)