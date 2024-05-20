'''
Created by sunwoong on 2024/05/20

풀이 시간 - 30분
'''
from collections import defaultdict

def solution(gems):
    origin = set()
    for gen in gems:
        origin.add(gen)
    promising = []
    seen = set()
    counting = defaultdict(int)
    prev_right = None
    left = right = 0
    while right < len(gems):
        if prev_right != right:
            seen.add(gems[right])
            counting[gems[right]] += 1
        prev_right = right
        if len(seen) == len(origin):
            promising.append([left + 1, right + 1, right - left])
            counting[gems[left]] -= 1
            if counting[gems[left]] == 0:
                seen.remove(gems[left])
            left += 1
        else:
            right += 1
    promising.sort(key=lambda x: (x[2], x[0]))
    return promising[0][:2]