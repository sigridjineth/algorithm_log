def solution(n, arr1, arr2):
    maps = []
    for i in range(n):
        element = bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' ')
        maps.append(element)
    return maps