'''
Created by sunwoong on 2022/12/20
'''

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for r in range(len(arr1)):
        for c in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[r][c] += arr1[r][k] * arr2[k][c]
    return answer