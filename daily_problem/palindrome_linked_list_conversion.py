# Palindrome Linked List List Conversion
# LEETCODE 234번

# Definition of singly-linkedList
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head: ListNode) -> bool:
    this_list = []

    while (head != None):
        val = head.val
        this_list.append(val)
        head = head.next
    
    if (this_list == this_list[::-1]):
        return True

    return False