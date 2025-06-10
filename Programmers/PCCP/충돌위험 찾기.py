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
    
from collections import Counter

def solution(points, routes):
    record = [[[] for _ in range(101)] for _ in range(101)]
    table = dict()
    
    for i in range(len(points)):
        table[i + 1] = points[i]

    for i in range(len(routes)):
        sequence = 1
        for j in range(len(routes[i]) - 1):
            route = routes[i]
            sr, sc = table[route[j]]
            er, ec = table[route[j + 1]]
            
            if j == 0:
                record[sr][sc].append(sequence)
            while sr != er or sc != ec:
                sequence += 1
                if sr != er:
                    if sr < er:
                        sr += 1
                        record[sr][sc].append(sequence)
                    else:
                        sr -= 1
                        record[sr][sc].append(sequence)
                    continue
                if sc != ec:
                    if sc < ec:
                        sc += 1
                        record[sr][sc].append(sequence)
                    else:
                        sc -= 1
                        record[sr][sc].append(sequence)
    
    count = 0
    for r in range(len(record)):
        for c in range(len(record[0])):
            time = record[r][c]
            if not time:
                continue
            time = Counter(time)
            counting = time.most_common()
            for item in counting:
                if item[1] > 1:
                    count += 1

    return count