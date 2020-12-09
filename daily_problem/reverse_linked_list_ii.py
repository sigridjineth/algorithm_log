# 역순 연결 리스트 II LEETCODE #92 반복 구조로 노드 뒤집기
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if (head is None) or (m == n):
            return head
        root = prev = ListNode(None) # call by reference
        root.next = head
        # prev, end assignment
        for _ in range(m - 1):
            prev = prev.next
        end = prev.next
        # iteration with reversing nodes
        for _ in range(n - m):
            start = prev.next
            prev.next = end.next
            end.next = end.next.next
            prev.next.next = start
        return root.next