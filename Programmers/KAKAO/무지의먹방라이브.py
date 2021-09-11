import heapq

def solution(food_times, k):
    if (sum(food_times) <= k):
        return -1
    priority_queue = []
    for idx in range(len(food_times)):
        heapq.heappush(priority_queue, (food_times[idx], idx + 1))
    answer = 0
    previous = 0
    length = len(food_times)
    while (answer + (priority_queue[0][0] - previous) * length) <= k:
        now = heapq.heappop(priority_queue)[0]
        answer += (now - previous) * length
        length -= 1
        previous = now
    return sorted(priority_queue, key = lambda x: x[1])[(k - answer) % length][1]
