class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList_primitive(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
        cur = parent
        return cur.next
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(-1) # cur.val을 비교할 때 None 타입이면 에러가 발생한다.
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next # 반드시 화살표를 옮겨보면서 비교해야 헷갈리지 않는다.
            # 이동한 다음번 head가 None일 수도 있기 때문에 존재 여부를 확인하고 cur와 head의 값을 비교해 cur이 더 작다면 그 다음 반복때 while 구문이 실행되지 않고 바로 교환이 진행되도록 한다.
            # cur = parent를 반드시 필요할 때만 돌아가도록 할 수 있는데 이 경우는 cur가 head보다 클 때만 하면 될 것 같다.
            if head and cur.val > head.val:
                cur = parent
        return parent.next

four = ListNode(4)
two = ListNode(2)
one = ListNode(1)
three = ListNode(3)

four.next = two
two.next = one
one.next = three

print(Solution().insertionSortList(four))