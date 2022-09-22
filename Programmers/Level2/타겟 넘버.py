'''
Created by sunwoong on 2022/09/22
'''

def dfs(numbers, target, start, case):
    if start == len(numbers):
        if target == case:
            return 1
        return 0
    count = 0
    count += dfs(numbers, target, start + 1, case + numbers[start])
    count += dfs(numbers, target, start + 1, case - numbers[start])
    return count

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer