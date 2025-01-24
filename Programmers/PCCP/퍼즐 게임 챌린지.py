'''
Created by sunwoong on 2025/01/24

'''
def solution(diffs, times, limit):
    low, high = 1, 100000
    answer = None
    
    while low <= high:
        total = 0
        level = (low + high) // 2
        for i in range(len(times)):
            if diffs[i] <= level:
                total += times[i]
            else:
                count = diffs[i] - level
                if i == 0:
                    total += count * times[i] + times[i]
                else:
                    total += count * (times[i] + times[i - 1]) + times[i]
        if total > limit:
            low = level + 1
        else:
            answer = level
            high = level - 1
    
    return answer
                