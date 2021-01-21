# 역순 연결 리스트 LEETCODE 206 Reverse Linked List
# 재귀를 이용한 아주 우아한 풀이이다.

def reverseList(self, head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if (node is not None):
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)