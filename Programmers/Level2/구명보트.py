'''
Created by sunwoong on 2024/06/24

풀이 시간 - 40분
'''

def solution(people, limit):
    left = 0
    right = len(people) - 1
    people.sort()
    answer = 0
    while left <= right:
        answer += 1
        weight = people[left] + people[right]
        if weight <= limit:
            left += 1
        right -= 1
    return answer