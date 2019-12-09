#백준 2798번 문제
n, m = list(map(int, input().split(" "))) #5 21
cards = list(map(int, input().split(" "))) #5 6 7 8 9

def compare():
    length = len(cards)
    compareArray = list()
    for i in range(0, length-1):
        for j in range(1, length-1):
            for k in range(2, length-1): #3중 반복문 활용
                sumscore = cards[i] + cards[j] + cards[k]
                print(sumscore, cards[i], cards[j], cards[k])
                if sumscore <= m: #m에 도달하기 전까지 너가 최고야.
                    compareArray.append(sumscore)
                    if (abs(sumscore[0] - m) > abs(sumscore[1] - m):
                        sumscore[0]
                    result = sumscore
                    print(result)
    return result

print(compare())