'''
Created by sunwoong on 2024/09/25
'''

from itertools import combinations
from bisect import bisect_left

def solution(dice):
    win = 0
    answer = None
    
    for a in combinations(range(len(dice)), len(dice) // 2):
        b = []
        for i in range(len(dice)):
            if i not in a:
                b.append(i)
        a_nums = None
        for i in a:
            if not a_nums:
                a_nums = dice[i]
                continue
            temp = []
            for num1 in a_nums:
                for num2 in dice[i]:
                    temp.append(num1 + num2)
            a_nums = temp
            
        b_nums = None
        for i in b:
            if not b_nums:
                b_nums = dice[i]
                continue
            temp = []
            for num1 in b_nums:
                for num2 in dice[i]:
                    temp.append(num1 + num2)
            b_nums = temp
        
        a_nums.sort()
        b_nums.sort()
        
        win_count = 0
        for a_num in a_nums:
            win_count += bisect_left(b_nums, a_num)
            
        if win < win_count:
            win = win_count
            answer = [num + 1 for num in a]
    
    return answer
    