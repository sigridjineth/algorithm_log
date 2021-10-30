import copy

def solution():
    n = int(input())
    a = list(input())
    b = []
    m = (n-1)//2
    answer = -27116
    
    for i in range(n):
        if (a[i].isdigit()):
            a[i] = [int(a[i]), 0]
        else:
            if (a[i] == "+"):
                a[i] = [0, 1]
            elif (a[i] == "-"):
                a[i] = [0, 2]
            elif (a[i] == "*"):
                a[i] = [0, 3]
    
    for s in range(1<<m):
        ok = True
        for i in range(m-1):
            if (s&(1<<i)>0 and s&(1<<(i+1))>0):
                ok = False
        if (ok is False):
            continue
        b = copy.deepcopy(a)
        for i in range(m):
            if (s&(1<<i)>0):
                k = 2*i+1
                if (b[k][1] == 1):
                    b[k-1][0] += b[k+1][0]
                    b[k][1] = -1
                    b[k+1][0] = 0
                elif (b[k][1] == 2):
                    b[k-1][0] -= b[k+1][0]
                    b[k][1] = -1
                    b[k+1][0] = 0
                elif (b[k][1] == 3):
                    b[k-1][0] *= b[k+1][0]
                    b[k][1] = -1
                    b[k+1][0] = 0
        # 곱하기 연산 진행
        c = []
        flag = False
        for j in range(n):
            if (flag == True):
                flag = False
                continue
            if (j % 2 == 0): # 처음 수에는 무적권...
                c.append(b[j])
            else:
                if (b[j][1] == -1):
                    # 무시! 그냥 지나간다!
                    flag = True
                    continue
                else:
                    if (b[j][1] == 3):
                        num = c[-1][0] * b[j + 1][0]
                        c.pop()
                        c.append([num, 0])
                        # 무시! 그냥 지나간다!
                        flag = True
                        continue
                    else:
                        c.append(b[j])
        res = c[0][0]
        m2 = (len(c)-1) // 2
        for j in range(m2):
            k = 2*j+1
            if (c[k][1] == 1):
                res += c[k+1][0]
            elif (c[k][1] == 2):
                res -= c[k+1][0]
            elif (c[k][1] == 3):
                res *= c[k+1][0]
        if (answer < res):
            answer = res
    return answer

print(solution())
