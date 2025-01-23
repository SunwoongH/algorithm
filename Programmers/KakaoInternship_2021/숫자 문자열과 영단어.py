'''
Created by sunwoong on 2025/01/23

'''

def solution(s):
    answer = ""
    words = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    ban = None
    for i in range(len(s)):
        if ban and ban > i:
            continue
        if s[i].isdigit():
            answer += s[i]
            continue
        for word in words.keys():
            if s[i:i + len(word)] == word:
                answer += str(words[word])
                ban = i + len(word) - 1
                break
    
    return int(answer)