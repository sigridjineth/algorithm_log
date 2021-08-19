def dfs(index, n, a, c, l, r, x):
    if (index == n):
        count = 0
        total = 0
        hard = -99999
        easy = -99999

        for i in range(n):
            if (c[i] == False):
                continue
            total += a[i]
            count += 1
            if (hard == -99999 or hard < a[i]):
                hard = a[i]
            if (easy == -99999 or easy > a[i]):
                easy = a[i]
        
        if (count >= 2 and l <= total <= r and (hard - easy) >= x):
            return 1
        else:
            return 0

    elif (index != n):
        c[index] = True
        count1 = dfs(index + 1, n, a, c, l, r, x)
        c[index] = False
        count2 = dfs(index + 1, n, a, c, l, r, x)
        return count1 + count2
    
def solution():
    n, l, r, x = map(int, input().split())
    a = list(map(int, input().split()))
    c = [False] * (n + 1)
    answer = dfs(0, n, a, c, l, r, x)
    return answer

print(solution())
