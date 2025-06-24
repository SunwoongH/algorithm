'''
Created by sunwoong on 2025/06/24
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

from itertools import permutations

def solution(n, weak, dist):
    answer = int(1e9)
    
    new_weak = weak[:]
    for i in range(len(weak) - 1):
        new_weak.append(n + weak[i])
    
    for case in permutations(dist, len(dist)):
        for i in range(len(weak)):
            start = i - 1
            for k in range(len(dist)):
                end = new_weak[start + 1] + case[k]
                while start + 1 < i + len(weak):
                    if new_weak[start + 1] <= end:
                        start += 1
                    else:
                        break
                if start == i + len(weak) - 1:
                    answer = min(answer, k + 1)
                    break
                    
    if answer == int(1e9):
        return -1
    
    return answer