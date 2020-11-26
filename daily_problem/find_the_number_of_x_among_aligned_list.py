# 정렬된 배열에서 특정 수의 개수 구하기
# 가장 왼쪽에 있는 원소 인덱스 구하기
def find_first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우, 가장 왼 쪽에 있는 경우에는 인덱스 반환
    if (array[mid] == target) and ((mid == 0) or (array[mid-1] < target)):
        return mid
    
    elif (array[mid] >= target):
        return find_first(array, target, start, mid - 1)
    
    else:
        return find_first(array, target, mid + 1, end)

# 가장 오른쪽에 있는 원소 인덱스 구하기
def find_last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우, 가장 왼 쪽에 있는 경우에는 인덱스 반환
    if (array[mid] == target) and ((mid == len(array)-1) or (array[mid+1] > target)):
        return mid
    
    elif (array[mid] > target):
        return find_first(array, target, start, mid - 1)
    
    else:
        return find_first(array, target, mid + 1, end)

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메소드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)
    # x가 처음 등장한 경우
    first_element = find_first(array, x, 0, n-1)
    # x가 마지막에 등장한 경우
    last_element = find_last(array, x, 0, n-1)
    # 없는 경우 분기 처리
    if (first_element == None) or (last_element == None):
        return None
    # 결과값 반환
    return abs(last_element - first_element + 1)

def solution():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    answer = count_by_value(data, m)
    if (answer == None):
        return -1
    else:
        print(answer)

print(solution())