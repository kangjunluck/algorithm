# LRU 알고리즘을 이해하고 있어야 한다.
# 주어진 크기 내에서 오래된 것이 교체되는 알고리즘
# cache miss 의 경우, cache 안에 없을 경우
# cache hit 의 경우, cache 안에 있을 경우

def solution(cacheSize, cities):
    answer = 0
    cities = [city.lower() for city in cities]
    cache = []
    time = 0
    if cacheSize == 0:
        time = 5 * len(cities)
    else:    
        for city in cities:
            # cache에 있는 경우
            if city in cache:
                # cache가 꽉 찬 경우
                idx = cache.index(city)
                cache.pop(idx)
                cache.append(city)
                time += 1
            # city가 cache에 없는 경우
            else:
                # cache가 꽉 찬 경우
                if len(cache) >= cacheSize:
                    cache.pop(0)
                    cache.append(city)
                # 덜찬 경우
                else:
                    cache.append(city)
                time += 5
    answer = time
    return answer