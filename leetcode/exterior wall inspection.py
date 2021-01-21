# exterior wall inspection

# 제한 조건을 보았을 때 리스트의 길이가 작으므로 완전 탐색으로 시행한다.
# 취약한 지점들이 원형으로 구성되어 있으므로 이를 처리하기 위해서 길이를 2배로 늘려서 원형을 일자 형태로 작업한다.

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘리자
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1 # 투입할 친구 수 초기화
    # 완전탐색 시작: 0에서 length -1까지를 출발점으로 설정
    for start in range(length):
        # 친구를 모두 나열하는데 수열을 사용
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 일단 1명을 투입
            # 마지막 check이 가능한 곳
            position = weak[start] + friends[count-1]
            # 가장 가까운 체크지점에서 지금 내가 갈 수 있는 최대 범위까지
            # 시작점부터 모든 취약지점을 확인한다. 점점 갈 수록 범위가 늘려간다.
            for index in range(start, start + length):
                # 점검 가능 위치를 벗어나는 경우
                if (position < weak[index]):
                    count += 1 # 1명 추가
                    # 만약 투입 불가하다면 종료 처리
                    if (count > len(dist)):
                        break
                    # 만약 투입이 가능하다면
                    else:
                        position = weak[start] + friends[count - 1]
                    # 비교 후 정답 update
                    answer = min(answer, count)
    if (answer > len(dist)):
        return -1
    return answer