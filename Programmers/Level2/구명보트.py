'''
Created by sunwoong on 2022/12/14
'''

def solution(people, limit):
    count = 0
    left, right = 0, len(people) - 1
    people.sort(reverse=True)
    while left <= right:
        boat = people[left]
        if left < right and boat + people[right] <= limit:
            right -= 1
        left += 1
        count += 1
    return count