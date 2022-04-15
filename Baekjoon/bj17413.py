'''
Created by sunwoong on 2022/04/15
'''
import sys

sentence = list(sys.stdin.readline().rstrip('\n'))
pivot, left, right, flag = 0, 0, 0, False
while pivot < len(sentence):
    if sentence[pivot] == '<':
        flag, right = True, pivot
        if left < right:
            temp = sentence[left:right]
            temp.reverse()
            print(''.join(temp), end='')
        left = pivot
    elif sentence[pivot] == '>':
        flag, right = False, pivot
        print(''.join(sentence[left:right + 1]), end='')
        left = pivot + 1
    elif not flag and sentence[pivot] == ' ':
        right = pivot
        temp = sentence[left:right]
        temp.reverse()
        print(''.join(temp), end=' ')
        left = pivot + 1
    pivot += 1
temp = sentence[left:pivot]
temp.reverse()
print(''.join(temp))