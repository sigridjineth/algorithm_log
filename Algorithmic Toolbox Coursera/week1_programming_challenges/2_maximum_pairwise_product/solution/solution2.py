def Max(array):
    array = sorted(array)
    while len(array) == n:
        print(array[n-1]*array[n-2])

n = int(input())
a = [int(x) for x in input().split()]

Max(a)