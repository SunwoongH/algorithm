'''
Created by sunwoong on 2024/08/09
'''
import heapq
import sys

def solution(alp, cop, problems):
    distance = [[sys.maxsize for _ in range(151)] for _ in range(151)]
    max_a = max(problems, key=lambda x: x[0])[0]
    max_b = max(problems, key=lambda x: x[1])[1]
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    
    heap = [(0, alp, cop)]
    while heap:
        cost, a, b = heapq.heappop(heap)
        if distance[a][b] < cost:
            continue
            
        if a >= max_a and b >= max_b:
            return distance[a][b]
        
        for need_a, need_b, ua, ub, ncost in problems:
            if a >= need_a and b >= need_b:
                da = min(150, a + ua)
                db = min(150, b + ub)
                if distance[da][db] > cost + ncost:
                    distance[da][db] = cost + ncost
                    heapq.heappush(heap, (distance[da][db], da, db))

def solution(alp, cop, problems):
    problems += [[0, 0, 0, 1, 1], [0, 0, 1, 0, 1]]
    max_a = max(problems, key=lambda x: x[0])[0]
    max_b = max(problems, key=lambda x: x[1])[1]
    dp = [[sys.maxsize for _ in range(max_b + 1)] for _ in range(max_a + 1)]
    
    alp = min(alp, max_a)
    cop = min(cop, max_b)
    
    dp[alp][cop] = 0
    for a in range(alp, max_a + 1):
        for b in range(cop, max_b + 1):
            for need_a, need_b, ua, ub, cost in problems:
                if a >= need_a and b >= need_b:
                    da = min(a + ua, max_a)
                    db = min(b + ub, max_b)
                    dp[da][db] = min(dp[da][db], dp[a][b] + cost)

    return dp[max_a][max_b]