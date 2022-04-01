'''
Created by sunwoong on 2022/04/01
'''
sequence = list(map(int, input().split()))
print('ascending') if sequence == [1, 2, 3, 4, 5, 6, 7, 8] else print('descending') if sequence == [8, 7, 6, 5, 4, 3, 2, 1] else print('mixed')