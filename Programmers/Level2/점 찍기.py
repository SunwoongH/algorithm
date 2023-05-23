'''
Created by sunwoong on 2023/05/23
'''

def solution(k, d):
    position = []
    answer = 0
    for i in range(d // k + 1):
        position.append(i * k)
    for i in range(d // k + 1):
        target = pow(d, 2) - pow(i * k, 2)
        low, high = 0, len(position) - 1
        while low <= high:
            mid = (low + high) // 2
            temp = pow(position[mid], 2)
            if temp <= target:
                low = mid + 1
            else:
                high = mid - 1
        answer += position[high] // k + 1
    return answer