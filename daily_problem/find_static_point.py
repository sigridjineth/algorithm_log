# 고정점 찾기
def find_static_point(array, start, end):
    if (start > end):
        return -1
    mid = (start + end) // 2
    if (array[mid] == mid):
        return mid
    elif (array[mid] > mid):
        return find_static_point(array, start, mid - 1)
    elif (array[mid] < mid):
        return find_static_point(array, mid + 1, end)
    else:
        return -1

def solution():
    n = int(input())
    data = list(map(int, input().split()))
    return find_static_point(data, 0, n - 1)

print(solution())