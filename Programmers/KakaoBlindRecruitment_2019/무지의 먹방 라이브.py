'''
Created by sunwoong on 2024/11/07
'''
from collections import defaultdict

def solution(food_times, k):
    seen = set(range(len(food_times)))
    
    counting = defaultdict(int)
    for i in range(len(food_times)):
        counting[i] = food_times[i]
    
    items = sorted(map(list, counting.items()), key=lambda x: x[1])
    
    prev = 0
    for item in items:
        need = (item[1] - prev) * len(seen)
        
        if need <= k:
            k -= need
            seen.remove(item[0])
            prev = item[1]
        else:
            break
    
    seen = sorted(seen)

    if not seen:
        return -1
    
    return seen[k % len(seen)] + 1
    