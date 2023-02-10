'''
Created by sunwoong on 2023/02/10

풀이 시간 - 9분
'''

def solution(lottos, win_nums):
    choice_count = 0
    is_lotto = 0
    ranking_table = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    for lotto in lottos:
        if not lotto:
            choice_count += 1
            continue
        if lotto in win_nums:
            is_lotto += 1
    return [ranking_table[is_lotto + choice_count], ranking_table[is_lotto]]