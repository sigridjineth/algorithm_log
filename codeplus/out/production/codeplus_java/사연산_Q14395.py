from collections import deque

limit = 1000000000
s,t = map(int,input().split())
check = set()
q = deque()
q.append((s,''))
check.add(s)
while q:
    x, s = q.popleft()
    if x == t:
        if len(s) == 0:
            s = '0'
        print(s)
        exit()
    if 0 <= x*x <= limit and x*x not in check:
        q.append((x*x,s+'*'))
        check.add(x*x)
    if 0 <= x+x <= limit and x+x not in check:
        q.append((x+x,s+'+'))
        check.add(x+x)
    if 0 <= x-x <= limit and x-x not in check:
        q.append((x-x,s+'-'))
        check.add(x-x)
    if x != 0 and 0 <= x//x <= limit and x//x not in check:
        q.append((x//x,s+'/'))
        check.add(x//x)
print(-1)
