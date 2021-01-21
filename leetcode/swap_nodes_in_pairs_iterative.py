# 페어의 노드 스왑 LEETCODE #24
# 반복 구조로 스왑
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while (head is not None) and (head.next is not None):
            # b to point head
            b = head.next
            head.next = b.next
            b.next = head
            
            # prev to point head
            prev.next = b
            
            # move to compare next comparison
            head = head.next
            prev = prev.next.next
        return root.next