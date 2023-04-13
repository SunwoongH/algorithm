'''
Created by sunwoong on 2023/04/13
'''
import heapq

def solution(n, k, enemy):
    heap = []
    answer = 0
    for i in range(len(enemy)):
        if k > 0:
            k -= 1
            heapq.heappush(heap, enemy[i])
            continue
        elif k == 0:
            temp = heapq.heappop(heap)
            if temp < enemy[i] and n >= temp:
                n -= temp
                heapq.heappush(heap, enemy[i])
                continue
            else:
                heapq.heappush(heap, temp)
        if n >= enemy[i]:
            n -= enemy[i]
        else:
            answer = i
            break
    return answer if answer else len(enemy)