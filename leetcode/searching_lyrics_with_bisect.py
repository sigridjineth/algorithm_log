# 가사 검색 카카오 2020: bisect 라이브러리 활용 나동빈님 답안 학습

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 경우에 대하여 길이를 갖는 메서드 생성
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    # 이진 탐색을 수행하기 위해 길이별로 정렬
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집는다

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if (q[0] != "?"):
            res = count_by_range(array[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        else:
            res = count_by_range(reversed_array[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        answer.append(res)

    return answer