# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()
        
        while (head != None):
            val = head.val
            q.append(val)
            head = head.next
            
        while (len(q) > 1):
            if (q.popleft() != q.pop()):
                return False
            
        return True