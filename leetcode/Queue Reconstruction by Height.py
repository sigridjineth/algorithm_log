import heapq

class Solution:
    # 우선순위 큐를 이용한다.
    # 첫 번째 값이 입력 예시에서 큰 순서대로 추출되는 Max Heap 형태로 풀이한다.
    # 그 이후에는 현재 추출된 요소들 중에서 두 번째 값을 인덱스로 활용하여 삽입한다.
    # 이는 큰 것부터 작은 것 순으로 삽입하다보면 자연스럽게 완성되는 풀이 과정이다.
    # 첫 번째 값을 음수로 변경해 최소 힙에서도 최대 힙처럼 구현할 수 있다.
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
    
        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
    
        return result