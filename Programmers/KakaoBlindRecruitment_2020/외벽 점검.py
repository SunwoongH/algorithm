'''
Created by sunwoong on 2024/10/09
'''
from itertools import permutations

def solution(n, weak, dist):
    route = weak[:]
    
    for i in range(len(weak) - 1):
        route.append(weak[i] + n)

    for i in range(1, len(dist) + 1):
        for case in permutations(dist, i):
            for j in range(len(weak)):
                distance = 0
                pos = 0
                visited = [False for _ in range(len(weak))]
                for k in range(len(weak)):
                    if k == 0:
                        distance += case[pos]
                        pos += 1
                        visited[k] = True
                        continue
                    move = route[j + k] - route[j + k - 1]
                    distance -= move
                    if distance < 0:
                        if pos < i:
                            distance = case[pos]
                            pos += 1
                            visited[k] = True
                        else:
                            break
                    else:
                        visited[k] = True
                if all(visited):
                    return i

    return -1