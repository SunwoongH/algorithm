'''
Created by sunwoong on 2024/06/25

풀이 시간 - 55분
'''
import heapq

def solution(routes):
    answer = 0
    road = []
    route_range = sum(routes, [])
    route_range.sort()
    routes.sort(reverse=True)
    for i in route_range:
        while routes and routes[-1][0] == i:
            route = routes.pop()
            heapq.heappush(road, (route[1], route))
        before_count = len(road)
        while road:
            time, route = heapq.heappop(road)
            if time != i:
                heapq.heappush(road, (time, route))
                break
        after_count = len(road)
        if before_count > after_count:
            answer += 1
            road.clear()
    return answer