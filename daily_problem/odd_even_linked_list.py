# Odd Even Linked List LEETCODE #328
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # exception
        if (head is None):
            return None
        
        # initialization
        odd = head # odd node start
        even = head.next # even node start
        even_head = head.next # initialization of even node
        
        # iteration with processing of odd nodes and even nodes
        while (even is not None) and (even.next is not None):
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        # connect the head of even node to the last of odd node
        odd.next = even_head
        return head