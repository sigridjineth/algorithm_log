# Sort List LEETCODE #148
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if (l1.val > l2.val):
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        # 런너 기법을 활용하여 연결 리스트의 중간과 끝을 파악하고 이를 바탕으로 절반씩 분할하자.
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None # half 다음을 끊어버림으로서 연결 리스트를 서로 분할한다.

        # 분할 재귀 호출
        l1 = self.sortList(head) # 첫째값인 head를 기준으로 분할한다. (좌측 분할)
        l2 = self.sortList(slow) # 중앙값인 slow를 기준으로 분할한다. (우측 분할)

        return self.mergeTwoLists(l1, l2)

    def sortList_Pythonic(self, head: ListNode) -> ListNode:
        # 연결 리스트를 파이썬 리스트로 바꾼다.
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
        # 팀 소트를 이용해서 매우 빠르다.
        lst.sort()
        # 파이썬 리스트를 연결 리스트로 바꾼다.
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head