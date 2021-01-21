# bracket converter 괄호 변환
# 특정 문자열에서 균형잡힌 괄호 문자열이 인덱스를 반환하는 함수 / 특정한 균형잡힌 괄호 문자열이 곧 올바른 괄호 문자열인지 판단하는 함수를 별도로 구현한다
# 재귀함수를 통해 두 함수를 불러오도록 한다.

# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    # 왼쪽 괄호의 개수
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        if p[i] == ')':
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    # 왼쪽 괄호의 개수
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if (count == 0):
                return False
            count -= 1
    return True

def solution(char):
    answer = ""
    # 빈 문자열이 들어왔으면 빈 문자열 리턴
    if (char == ""):
        return answer
    # 문자열 w를 두 "균형 잡힌 괄호 문자열" u와 v로 분리한다
    index = balanced_index(char)
    u = char[0:index+1]
    v = char[index+1:]
    # u가 "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if (check_proper(u)):
        answer = u + solution(v)
    # u가 "올바른 괄호 문자열"이 아니라면, 다음의 단계를 수행
    else:
        # 4-1
        answer = "("
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ")"
        # 4-4
        u = list(u[1:-1])
        for i in range(len(u)):
            if (u[i] == "("):
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    
    return answer