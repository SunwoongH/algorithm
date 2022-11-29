'''
Created by sunwoong on 2022/11/29
'''

from collections import defaultdict

def solution(want, number, discount):
    origin = defaultdict(int)
    for i in range(len(want)):
        origin[want[i]] = number[i]
    count = defaultdict(int)
    answer = 0
    left = right = 0
    while right < len(discount):
        if right - left < 9:
            count[discount[right]] += 1
            right += 1
            continue
        count[discount[right]] += 1
        answer += 1 if all(map(lambda x: count[x] == origin[x], want)) else 0
        count[discount[left]] -= 1
        left += 1
        right += 1
    return answer