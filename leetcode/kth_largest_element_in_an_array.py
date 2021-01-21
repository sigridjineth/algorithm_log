# LEETCODE 215
# 배열의 K번째로 큰 요소
class Solution:
    # heapq 모듈 이용
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        for _ in range(0, k-1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)
    # heapq 모듈의 heapify 이용
    # heapify()는 주어진 자료구조가 힙 특성을 만족하도록 바꿔주는 연산이다.
    def findKthLargest_Heapify(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
    # heapq 모듈의 nlargest 이용
    # nlargest, nsmallest 함수를 이용하면 0부터 최대 n까지 largest/smallest한 녀석을 반환한다.
    # 따라서 여기에서는 맨 마지막 리스트 원소를 반환하기 위해 인덱스 -1을 이용했다.
    def findKthLargest_NLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
    # 정렬을 이용한 풀이
    # 직관적으로 풀이할 수 있고 파이썬의 정렬 함수가 팀 소트니까 속도도 제일 빠르다.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]