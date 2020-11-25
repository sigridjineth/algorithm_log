# 실패율
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시킨다
    for i in range(1, N+1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        failure_rate = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, failure_rate))

        # 다음 스테이지에 머물러 있는 사람의 수는 전체 사람 수 중에서 현재 스테이지에 머물러 있는 사람의 수 
        length -= count
        
        # 실패율을 기준으로 각 스테이지를 내림차순 정렬
        answer = sorted(answer, key = lambda x: -x[1])
        # answer = sorted(answer, key = lambda x: x[1], reverse = True)

        # 정렬된 스테이지 번호 출력
        answer = [i[0] for i in answer]
        print(answer)

solution(5, [2,1,2,6,2,4,3,3])