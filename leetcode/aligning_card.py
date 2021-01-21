# 카드 정렬하기
import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    card = int(input())
    heapq.heappush(heap, card)

result = 0

# 힙(Heap)에 원소가 두 개 남을 때까지 반복
while (len(heap) > 2):
    now = heapq.heappop(heap)
    next = heapq.heappop(heap)
    combined = now + next
    result += combined
    heapq.heappush(heap, combined)

if (len(heap) == 2):
    now = heapq.heappop(heap)
    next = heapq.heappop(heap)
    result += (now + next)

print(result)