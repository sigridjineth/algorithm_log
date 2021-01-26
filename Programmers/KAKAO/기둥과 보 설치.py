# 기둥과 보 설치
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, what, how = frame
        if (how == 1): # 설치
            answer.append([x, y, what])
            if (check(answer) is False):
                answer.remove([x, y, what])
        else:
            answer.remove([x, y, what])
            if (check(answer) is False):
                answer.append([x, y, what])
    answer.sort()
    return answer

def check(answer):
    for x, y, what in answer:
        if (what == 0): # 기둥
            if (y == 0 or [x-1, y, 1] in answer or [x, y-1, 0] in answer or [x, y, 1] in answer):
                continue
            else:
                return False
        elif (what == 1): # 보
            if (([x-1, y, 1] in answer and [x+1, y, 1] in answer) or ([x, y-1, 0] in answer) or ([x+1, y-1, 0] in answer)):
                continue
            else:
                return False
    return True