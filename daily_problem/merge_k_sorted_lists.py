# k개 정렬 리스트 병합 LEETCODE #23
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        
        for i in range(len(lists)):
            if (lists[i]):
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            if (result.next):
                heapq.heappush(heap, (result.next.val, idx, result.next))
                
        return root.next