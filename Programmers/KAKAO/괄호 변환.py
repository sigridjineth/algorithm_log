# 카카오 2020 괄호 변환
# 균형잡힌 문자열의 인덱스를 반환하는 함수
def balanced_index(p):
    # 왼쪽 괄호 "(" 의 개수
    count = 0
    for i in range(len(p)):
        if (p[i] == "("):
            count += 1
        else:
            count -= 1
        if (count == 0): # 균형잡힌 문자열로 더 분리할 수 없어야 하므로 가장 최근에 발견된 인덱스 반환 요망
            return i
# 올바른 괄호 문자열인지 판단하는 함수
def proper_check(p):
    # 왼쪽 괄호 "(" 의 개수
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if (count == 0): # 쌍이 맞지 않는 경우이므로 False를 리턴한다
                return False
            else: # 쌍이 맞는 경우 이므로 계속 탐색한다
                count -= 1
    if (count == 0): # 쌍이 맞는 경우
        return True
def solution(p):
    answer = ""
    if (p == ""):
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    # 만약 올바른 괄호 문자열이라면, v에 대해 재귀적으로 수행한다
    if proper_check(u):
        answer = u + solution(v)
    # 만약 올바른 괄호 문자열이 아니라면, 문제에 나와있는 대로 수행한다
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1]) # 맨 처음과 마지막 문자를 제거
        for i in range(len(u)):
            if (u[i] == "("):
                u[i] = ")"
            elif (u[i] == ")"):
                u[i] = "("
        answer += "".join(u)
    return answer