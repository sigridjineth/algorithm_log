from collections import deque

s = []
for i in range(3):
    temp = input().split()
    cnt = int(temp[0])
    if cnt > 0:
        s.append(temp[1])
    else:
        s.append('')
        
cnt = [0,0,0]
for i in range(3):
    for ch in s[i]:
        cnt[ord(ch)-ord('A')] += 1
        
d = dict()
q = deque()
q.append(tuple(s))
d[tuple(s)] = 0

while q:
    x = q.popleft()
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if len(x[i]) == 0:
                continue
            y = list(x[:])
            y[j] = y[j] + x[i][-1]
            y[i] = y[i][:-1]
            y = tuple(y)
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)

ans = ['', '', '']

for i in range(3):
    for j in range(cnt[i]):
        ans[i] += chr(ord('A')+i)
print(d[tuple(ans)])
