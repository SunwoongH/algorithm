'''
Created by sunwoong on 2022/05/03
'''
import sys
import collections

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    word = list(sys.stdin.readline().split())
    new_word = collections.deque([word[0]])
    for i in range(1, len(word)):
        if word[i] <= new_word[0]:
            new_word.appendleft(word[i])
        else:
            new_word.append(word[i])
    print(''.join(new_word))