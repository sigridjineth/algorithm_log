import sys

def last_digit(n):
    if n<1:
        return n
    prev=0
    curr=1
    
    for i in range(n-1):
        prev, curr = curr%10, (prev+curr)%10
    return curr%10

def sum_squares(n):
    