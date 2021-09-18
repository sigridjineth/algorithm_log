def solution():
    limit = 10000
    nums = [1, 2, 3]
    d = [0] * (limit + 1)
    d[0] = 1

    for i in range(1, limit + 1):
        for j in range(0, len(nums)):
            if (i - nums[j] >= 0):
                d[i] += d[i - nums[j]]

    t = int(input())
    answer = ""
    for _ in range(t):
        n = int(input())
        answer += (str(d[n]) + '\n')
    
    return answer

print(solution())
