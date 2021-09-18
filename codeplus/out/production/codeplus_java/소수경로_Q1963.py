#!/usr/bin/python3
from collections import deque

def change(num, index, digit):
    if index == 0 and digit == 0:
        return -1
    s = list(str(num))
    s[index] = chr(digit+ord('0'))
    return int(''.join(s))
prime = [False] * 10001

for i in range(2, 10001):
    if prime[i] == False:
        for j in range(i*i, 10001, i):
            prime[j] = True

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    c = [False] * 10001
    d = [0] * 10001
    d[n] = 0
    c[n] = True
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        for i in range(4):
            for j in range(10):
                nxt = change(now, i, j)
                if nxt != -1:
                    if prime[nxt] == False and c[nxt] == False:
                        q.append(nxt)
                        d[nxt] = d[now] + 1
                        c[nxt] = True
    print(d[m])
