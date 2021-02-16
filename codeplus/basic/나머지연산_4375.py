# 백준 4375번 1

while True:
    try:
        n = int(input())
    except:
        break

    num = 0
    i = 1
    
    while True:
        num = num * 10 + 1
        num %= n
        if (num == 0):
            print(i)
            break
        i += 1