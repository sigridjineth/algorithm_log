import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k초가 크다면 무시
    if (sum(food_times) <= k):
        return -1
    # 시간이 작은 음식이 빨리 사라지니깐 얘부터 삭제한다. 우선순위 큐로 최소 힙 이용한다.
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
        # 지금까지 다 처먹은 시간
        sum_value = 0
        # 이전에 모두 먹기 완료한 음식의 시간
        previous = 0
        # 남은 음식의 개수
        length = len(food_times)
    
    # (지금까지 다 처먹은 시간) + (현재 음식 시간 - 현재 음식 시간 중 이미 먹은 시간 - 즉 이전에 모두 먹기 완료한 음식의 시간) * 현재 남아있는 음식의 개수와 K초를 비교한다.
    while ((sum_value) + ((q[0][0] - previous)) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    # 음식의 번호대로 정렬
    result = sorted(q, key=lambda element: element[1])
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    return result[(k - sum_value) % length][1]
