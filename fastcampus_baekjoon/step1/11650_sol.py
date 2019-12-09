n = int(input())
array = []

for _ in range(n):
    x, y = input().split(" ")
    thisloca = {"x": int(x), "y": int(y)}
    array.append(thisloca)

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i]["x"] > array[j]["x"]:
            array[i], array[j] = array[j], array[i]
        elif array[i]["x"] == array[j]["x"]:
            if array[i]["y"] > array[j]["y"]:
                array[i], array[j] = array[j], array[i]

for value in array:
    temp = [value, value]
    print(temp)