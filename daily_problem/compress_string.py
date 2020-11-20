# 문자열 압축
def solution(s):
    # 정답을 문자열 개수로 초기화
    answer = len(s)
    # 1개 단위(step) 별로 단위를 늘려가며 압축 범위를 확인
    # 2 * (문자열) 이 되어야 최소한으로 의미가 있으므로 늘려가는 체크 범위를 첫 번째 원소부터 절반까지로 설정
    for step in range(1, len(s) // 2 + 1):
        # 매번 새로운 스텝을 체크할 때마다 압축되는 문자열 초기화
        compressed = ""
        # 앞에서부터 step 만큼의 문자열 추출 후 초기화
        prev = s[0:step]
        # 현재 문자열 체크하는 단계의 횟수를 1로 초기화
        count = 1
        step = 0
        # step부터 출발하여 단위를 step만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s) + 1, step):
            # 만약 일치한다면, 일치 횟수를 1 증가
            next = s[j:j+step]
            if (prev == next):
                count += 1
            # 다른 문자열이 나와 더 이상 압축하지 못하는 경우라면, compressed를 업뎃하고 다음 step으로 넘어간다
            else:
                if (count >= 2):
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                # 상태를 다시 초기화한다
                    prev = next
                    count = 1
            left = j
            # step의 한계로 더 이상 진행하지 못하고 남아있는 문자열 처리
            if (left < len(s) + 1):
                current_length = len(s)
                compressed += (s[left:current_length])
            
            # 만들어지는 압축 문자열이 가장 짧은 것이 정답
            answer = min(answer, len(compressed))

            return answer