import collections, re

def solution(str1, str2):
    # 두 글자씩 끊어보자
    new_str1 = [
        # 리스트 컴프리헨션 처리
        str1[i:i+2].lower()
        for i in range(len(str1)-1)
        if re.findall('[a-z]{2}', str1[i:i+2].lower()) # regex 처리
    ]
    new_str2 = [
        # 리스트 컴프리헨션 처리
        str2[i:i+2].lower()
        for i in range(len(str2)-1)
        if re.findall('[a-z]{2}', str2[i:i+2].lower()) # regex 처리
    ]
    # 교집합 계산
    # collections.Counter(new_str1) 등으로 각자 리스트의 counter를 계산한다.
    # 이후 AND 연산을 해서 나오는 dictionary 형태를 values로 따온다.
    # 마지막으로 이를 sum하여 교집합의 결과를 계산한다.
    intersection = sum((collections.Counter(new_str1) & collections.Counter(new_str2)).values())

    # 합집합 계산
    union = sum((collections.Counter(new_str1) | collections.Counter(new_str2)).values())

    jac = 1

    if (union == 0):
        return int(jac * 65536)
    else:
        jac = intersection / union
        return int(jac * 65536)

print(solution('FRANCE', 'french'))