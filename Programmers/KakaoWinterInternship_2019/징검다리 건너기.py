'''
Created by sunwoong on 2024/04/25

풀이 시간 - 120분
'''

def solution(stones, k):
    answer = None
    low, high = 1, max(stones)
    while low <= high:
        mid = (low + high) // 2
        chance = k
        available = True
        for stone in stones:
            if stone - mid < 0:
                chance -= 1
            else:
                chance = k
            if chance == 0:
                available = False
                break
        if not available:
            high = mid - 1
        else:
            answer = mid
            low = mid + 1
    return answer