'''
Created by sunwoong on 2025/01/26
'''

from collections import Counter

def calculate_path(points, route):
    t = 0
    path = []
    
    for i in range(len(route) - 1):
        sr, sc = points[route[i] - 1]
        er, ec = points[route[i + 1] - 1]
        while sr != er:
            path.append((sr, sc, t))
            if sr > er:
                sr -= 1
            else:
                sr += 1
            t += 1
        while sc != ec:
            path.append((sr, sc, t))
            if sc > ec:
                sc -= 1
            else:
                sc += 1
            t += 1
    path.append((sr, sc, t))
    return path

def solution(points, routes):
    path = []
    
    for route in routes:
        path.extend(calculate_path(points, route))
    
    counting = Counter(path)
    answer = 0
    for count in counting.values():
        if count > 1:
            answer += 1
            
    return answer
    