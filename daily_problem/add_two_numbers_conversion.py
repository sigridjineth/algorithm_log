# 두 수의 덧셈 자료형 변환 리트코드 2번

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + \
                + int(''.join(str(e) for e in b))
            
        return self.toReversedLinkedList(str(resultStr)))