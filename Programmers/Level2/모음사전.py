'''
Created by sunwoong on 2024/03/21

풀이 시간 - 20분
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

alpha = ['A', 'E', 'I', 'O', 'U']

def dfs(word, target):
    if word == target:
        return 1, True
    count = 1
    found = False
    for char in alpha:
        word.append(char)
        if len(word) > 5:
            word.pop()
            continue
        prev_count, prev_found = dfs(word, target)
        count += prev_count
        word.pop()
        if prev_found:
            found = True
        if found:
            return count, found
    return count, found

def solution(word):
    return dfs([], list(word))[0] - 1