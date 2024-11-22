'''
Created by sunwoong on 2024/11/22

'''
from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    cache = deque()

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.appendleft(city)
            continue
        if len(cache) == cacheSize:
            cache.pop()
            cache.appendleft(city)
        else:
            cache.appendleft(city)
        answer += 5
        
    return answer