'''
Created by sunwoong on 2024/07/29

풀이 시간 - 34분
'''
import heapq

def solution(operations):
    removed = set()
    min_heap = []
    max_heap = []
    answer = [0, 0]
    for i, oper in enumerate(operations):
        char, num = oper.split()
        num = int(num)
        if char == 'I':
            heapq.heappush(min_heap, (num, num, i))
            heapq.heappush(max_heap, (-num, num, i))
            continue
        if num == 1:
            while max_heap:
                p, num, k = heapq.heappop(max_heap)
                if k not in removed:
                    removed.add(k)
                    break
        else:
            while min_heap:
                p, num, k = heapq.heappop(min_heap)
                if k not in removed:
                    removed.add(k)
                    break
    while max_heap:
        p, num, k = heapq.heappop(max_heap)
        if k not in removed:
            answer[0] = num
            break
    while min_heap:
        p, num, k = heapq.heappop(min_heap)
        if k not in removed:
            answer[1] = num
            break
    return answer