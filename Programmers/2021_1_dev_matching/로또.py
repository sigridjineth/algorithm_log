def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    count_zero = lottos.count(0)
    matches = 0
    for element in win_nums:
        if (element in lottos):
            matches = matches + 1
    return rank[count_zero + matches], rank[matches]
