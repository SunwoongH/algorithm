'''
Created by sunwoong on 2024/04/26

풀이 시간 - 180분
'''

def solution(distance, rocks, n):
    answer = None
    low, high = 1, distance
    rocks.append(distance)
    rocks.sort()
    while low <= high:
        mid = (low + high) // 2
        temp = 0
        count = 0
        for rock in rocks:
            if rock - temp < mid:
                count += 1
            else:
                temp = rock
            if count > n:
                break
        if count > n:
            high = mid - 1
        else:
            answer = mid
            low = mid + 1
    return answer