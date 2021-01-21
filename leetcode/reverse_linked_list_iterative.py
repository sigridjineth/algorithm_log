# 역순 연결 리스트 LEETCODE 206
# 반복 구조를 이용한 풀이. 가독성이 좋다.
def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None

    while (node is not None):
        next, node.next = node.next, prev
        prev, node = node, next

    return prev