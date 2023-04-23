# 페이지 교체 알고리즘 중 LRU 다음 사이트 참고 --> https://velog.io/@ddyy094/LRULeast-Recently-Used-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EB%9E%80
# *Cache Hit 이란?
# CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우, Cache Hit이라고 한다.
# * Cache Miss란?
# CPU가 참조하고자 하는 메모리가 캐시에 존재하지 않을 떄는 Cache Miss라고 함.
# 삽입이 아닌 삭제 개념을 사용해야 함.

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    lower_cities = [city.casefold() for city in cities]
    running_time = 0
    queue = deque()
    for city in lower_cities:
        if city not in queue:
            if len(queue) >= cacheSize:
                queue.popleft()
            queue.append(city)
            running_time += 5
        else:
            queue.remove(city)
            queue.append(city)
            running_time += 1
    return running_time

print(solution(	5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))


# 다른 사람의 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time