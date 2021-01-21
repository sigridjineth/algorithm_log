# columns and beams

# 일일이 전체 구조물을 확인하며 현재의 구조물이 정상인지 매 연산마다 메소드를 호출 및 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
            if (y == 0) or ([x-1,y,1] in answer) or ([x+1,y,1] in answer) or ([x,y-1,0] in answer):
                continue
            return False
        elif stuff == 1:
            # 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시에 연결
            if ([x, y-1, 0] in answer) or ([x+1, y-1, 0] in answer) or ([x+1,y,1] in answer) or ([x-1,y,1] in answer):
                continue
            return False
    return True
    
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if (operate == 0): # 삭제하는 경우
            answer.remove([x, y, stuff])
            if not (possible(answer)):
                answer.append([x, y, stuff])
        else:
            answer.append([x, y, stuff])
            if not (possible(answer)):
                answer.remove([x, y, stuff])
    return sorted(answer)