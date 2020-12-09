# 페어의 노드 스왑. LEETCODE #24
# 재귀 구조로 스왑
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (head is not None) and (head.next is not None):
            p = head.next
            # return swapped value
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head