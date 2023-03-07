'''
Created by sunwoong on 2023/03/07
'''
from collections import deque

def solution1(number, k):
    number = deque(number)
    seen = []
    count = 0
    length = len(number)
    while count < length and k != 0:
        if length - count == k:
            if seen and int(seen[-1]) < int(number[0]):
                number.appendleft(seen.pop())
                count -= 1
            number.popleft()
            count += 1
            k -= 1
            continue
        if int(number[0]) < int(number[1]):
            a = number.popleft()
            if seen and int(seen[-1]) < int(number[0]):
                number.appendleft(seen.pop())
                count -= 1
            count += 1
            k -= 1
        else:
            seen.append(number.popleft())
            count += 1
    answer = seen + list(number)
    idx = len(answer) - 1
    for i in range(len(answer)):
        if answer[i] != "0":
            idx = i
            break
    return ''.join(answer[idx:])

def solution2(number, k):
    answer = [number[0]]
    for i in range(1, len(number)):
        while k > 0 and answer and int(answer[-1]) < int(number[i]):
            answer.pop()
            k -= 1
        answer.append(number[i])
    return ''.join(answer[:len(answer) - k])