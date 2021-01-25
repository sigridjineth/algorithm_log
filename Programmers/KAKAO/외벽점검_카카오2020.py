# 외벽점검 카카오 2020
import copy
from itertools import permutations
from functools import reduce

def flatten_curve(n, weak, dist):
    def reducer(acc, cur):
        acc.append(cur + n)
        return acc
    flatten_weak = reduce(reducer, weak, copy.deepcopy(weak))
    return flatten_weak

def check_by_start_index(start, flatten_weak, dist, friends_list, length):
    answer = len(dist) + 1
    for friends in friends_list:
        count = 1
        final_position = flatten_weak[start] + friends[count-1]
        for index in range(start, start+length):
            if (final_position < flatten_weak[index]):
                count += 1
                if (count > len(dist)):
                    break
                final_position = flatten_weak[index] + friends[count-1]
        answer = min(answer, count)
    return answer

def solution(n, weak, dist):
    flatten_weak = flatten_curve(n, weak, dist)
    friends_list = list(permutations(dist, len(dist)))
    length = len(weak)

    answer = len(dist) + 1

    for start in range(length):
        answer = min(check_by_start_index(start, flatten_weak, dist, friends_list, length), answer)
    
    if answer > len(dist):
        return -1

    return answer

print(solution(12, [1,5,6,10], [1,2,3,4]))