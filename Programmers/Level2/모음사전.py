'''
Created by sunwoong on 2022/12/13
'''
from itertools import product

def solution(word):
    length = 5
    words = []
    for i in range(1, length + 1):
        for item in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(item))
    words.sort()
    for i in range(len(words)):
        if words[i] == word:
            return i + 1