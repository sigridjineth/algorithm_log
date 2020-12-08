# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        carry = 0
        while (l1 is not None) or (l2 is not None) or (carry > 0):
            sum = 0
            if (l1 is not None):
                sum += l1.val
                l1 = l1.next
            if (l2 is not None):
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next