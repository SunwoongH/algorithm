'''
Created by sunwoong on 2022/11/25
'''

def solution(topping):
    left = [0 for _ in range(len(topping))]
    right = [0 for _ in range(len(topping))]
    left[0] = 1
    left_seen, right_seen = set(), set()
    left_seen.add(topping[0])
    for i in range(1, len(topping)):
        left[i] = left[i - 1]
        if topping[i] not in left_seen:
            left_seen.add(topping[i])
            left[i] += 1
    for i in range(len(topping) - 2, -1, -1):
        right[i] = right[i + 1]
        if topping[i + 1] not in right_seen:
            right_seen.add(topping[i + 1])
            right[i] += 1
    answer = 0
    for i in range(len(topping)):
        if left[i] == right[i]:
            answer += 1
    return answer