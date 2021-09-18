def solution_next_permutation():
    a, b = input().split()
    a = list(a)
    b = int(b)
    ans = -1
    a.sort()

    def next_permutation(a):
        i = len(a) - 1
        while (i > 0 and a[i - 1] >= a[i]):
            i -= 1
        if (i <= 0):
            return False
        
        j = len(a) - 1
        while (a[j] <= a[i - 1]):
            j -= 1
        a[i - 1], a[j] = a[j], a[i - 1]
        
        j = len(a) - 1
        while (i < j):
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        return True

    while True:
        c = int("".join(a))
        if (c < b and a[0] != "0"):
            if (ans == -1 or ans < c):
                ans = c
        if (next_permutation(a) == False):
            break  
            # a has already changed after executing next_permutation function

    return ans

# print(solution_next_permutation())

def solution_recursive():
    a, b = input().split()
    a = list(map(int, a))
    n = len(a)
    b = int(b)
    check = [False] * n

    def dfs(index, num):
        if (index == n):
            return num
        elif (index != n):
            ans = -1
            for i in range(n):
                if (check[i]):
                    continue
                if (index == 0 and a[i] == 0):
                    continue
                check[i] = True
                temp = dfs(index + 1, num * 10 + a[i])
                if (temp < b):
                    if (ans == -1 or ans < temp):
                        ans = max(ans, temp)
                check[i] = False
        return ans

    answer = dfs(0, 0)
    return answer

print(solution_recursive())
