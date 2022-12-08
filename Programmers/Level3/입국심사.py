'''
Created by sunwoong on 2022/12/08
'''

def number_of_people_available(target, times):
    count = 0
    for time in times:
        count += target // time
    return count

def solution(n, times):
    low, high = 1, max(times) * n
    while low <= high:
        mid = (low + high) // 2
        count = number_of_people_available(mid, times)
        if count < n:
            low = mid + 1
        else:
            high = mid - 1
    return low