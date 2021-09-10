import collections

def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if (city in cache):
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer
