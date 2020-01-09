import sys
def pib(n):
    if n<1:
        return n
    else:
        prev=0
        curr=1
        for _ in range(n-1):
            prev,curr = curr, prev+curr
        return curr

def get_pisano(m):
    prev=0
    curr=1
    for i in range(m):
        prev, curr = curr, (prev+curr)%m