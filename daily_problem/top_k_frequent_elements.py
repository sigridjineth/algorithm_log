import heapq

def solution(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    # insert heap as minus value
    for f in freqs:
        # heapq align according to key value
        heapq.heappush(freqs_heap, (-freqs[f], f)) # python only support min-heap
        # uses minus value to let bigger value to be on the front
    topk = [] # topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk