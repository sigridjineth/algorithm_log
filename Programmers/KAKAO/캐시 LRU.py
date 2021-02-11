import collections

def solution(cacheSize, cities):
    elasped = 0
    caches = collections.deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        # 캐시 히트 시 재삽입 처리
        if city in caches:
            caches.remove(city)
            caches.append(city)
            elasped += 1
        else: # 캐시 미스 시 삽입만
            caches.append(city) # 만약 deque가 아니라면 앞쪽을 shift해야 한다
            elasped += 5
    return elasped